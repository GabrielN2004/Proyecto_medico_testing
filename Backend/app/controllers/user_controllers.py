from ..models.user_models import Usuarios
from flask import request, jsonify
from ..controllers.auth import Auth

class UsuarioController:
    """Clase controller de usuario"""

    @classmethod
    def create_usuario(cls):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No se proporcionaron datos'}), 400
        
        usuario_email = data.get('email')
        usuario_password = data.get('password')
        id_role = data.get('id_role')

        print(f"Recibido id_role: {id_role}")

        if not id_role:
            return jsonify({"error": "id_role is required"}), 400
        
        if not usuario_email or not usuario_password or id_role is None:
            return jsonify({'error': 'Faltan datos requeridos'}), 400
        
        usuario = Usuarios(usuario_email=usuario_email, usuario_password=usuario_password, id_role=id_role)
        print(usuario)
        Usuarios.usuario_create(usuario)
        
        response = {'message': 'Usuario creado exitosamente'}
        
        if id_role == 3:  # Solo si el usuario es paciente
            token = Auth.encode_auth_token(usuario_email, 'paciente')
            if token:
                response['token'] = token
        
        return jsonify(response), 201

    @classmethod
    def get_token_usuario(cls):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No se proporcionaron datos'}), 400
        
        usuario_email = data.get('usuario_email')
        
        if not usuario_email:
            return jsonify({'error': 'Falta el email del usuario'}), 400
        
        token = Auth.encode_auth_token(usuario_email, 'paciente')
        if not token:
            return jsonify({'error': 'No se pudo generar el token'}), 500
        
        return jsonify({'token': token}), 200
    
        