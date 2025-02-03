from flask import Flask, request, jsonify
from ..controllers.auth import Auth
from ..models.authenticate_user import AuthenticateUser
import jwt
class AuthContext:
    @classmethod
    def login(cls):
        """Genera un token JWT para el usuario autenticado."""
        data = request.get_json()

        if not data or not data.get('email') or not data.get('password'):
            return jsonify({'message': 'Correo electrónico y contraseña son requeridos'}), 400
        
        # Autenticación del usuario y obtención de user_id y role_name
        user_data = AuthenticateUser.authenticate_user(data['email'], data['password'])

        if not user_data:
            return jsonify({'message': 'Credenciales inválidas'}), 401

        id_usuario = user_data['id_usuario']
        role_name = user_data['role_name']

        # Generar el token JWT, incluyendo el rol del usuario
        token = Auth.encode_auth_token(id_usuario, role_name)

        if token:
            return jsonify({'token': token}), 200
        return jsonify({'message': 'Error al generar el token'}), 500


    @classmethod
    def protected(cls):
        """Ruta protegida que requiere un token de autenticación."""
        # Obtenemos el token de la cabecera Authorization
        auth_token = request.headers.get('Authorization')

        if not auth_token:
            return jsonify({'message': 'Token requerido'}), 403

        try:
            # Intentamos decodificar el token
            token = auth_token.split(" ")[1]  # Obtener el token después de 'Bearer'
            id_usuario = Auth.decode_auth_token(token)  # Devuelve el id_usuario o None si es inválido

            if id_usuario:
                # El token es válido, se devuelve un mensaje con la información del usuario
                return jsonify({'message': f'Bienvenido, usuario {id_usuario}'}), 200
            else:
                # El token no es válido o ha expirado
                return jsonify({'message': 'Token inválido o expirado'}), 401

        except IndexError:
            # Si el formato 'Bearer <token>' no es correcto
            return jsonify({'message': 'Formato de token incorrecto. Debe ser "Bearer <token>"'}), 400
        except jwt.ExpiredSignatureError:
            # El token ha expirado
            return jsonify({'message': 'El token ha expirado'}), 401
        except jwt.InvalidTokenError:
            # El token es inválido
            return jsonify({'message': 'Token inválido'}), 401
