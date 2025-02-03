from ..models.paciente_models import Pacientes
from ..models.turno_models import Turnos
from ..models.profesional_models import Profesional
from flask import request, jsonify
from functools import wraps
import jwt
from datetime import datetime, timedelta

# Función para verificar el token de autenticación
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token de autenticación es requerido'}), 403
        try:
            token = token.split(" ")[1]  # Se espera que el token esté precedido por 'Bearer'
            decoded_token = jwt.decode(token, 'SECRET_KEY', algorithms=['HS256'])  # Se verifica con la clave secreta
            current_user = decoded_token['id_usuario']  # El id del usuario está en el payload del token
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'El token ha expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token inválido'}), 403
        return f(current_user, *args, **kwargs)
    return decorated_function

class ProfilePaciente:
    @classmethod
    def profilepaciente(cls):
        dni_paciente = request.args.get('dni_paciente')
        if dni_paciente:
            paciente = Pacientes.get_paciente(dni_paciente)
            turnos = Turnos.get_turnos_by_paciente(dni_paciente)
            if paciente:
                return jsonify({
                    'paciente': paciente,
                    'turnos': turnos
                }), 200
            else:
                return jsonify({
                    'error': 'Paciente no encontrado'
                }), 404
        else:
            return jsonify({
                'error': 'DNI del paciente es requerido'
            }), 400

    @classmethod
    @token_required
    def modificar(cls, current_user):
        data = request.get_json()
        dni_paciente = data.get('dni_paciente')
        if dni_paciente:
            paciente = Pacientes.get_paciente(dni_paciente)
            if paciente:
                update_data = Pacientes()
                update_data.paciente_name = data.get('nombre')
                update_data.paciente_lastname = data.get('apellido')
                update_data.paciente_email = data.get('email')
                update_data.paciente_password = data.get('password', paciente.paciente_password)  # No actualiza si no se pasa
                update_data.id_obrasocial = data.get('obrasocial')
                update_data.dni_paciente = dni_paciente  # Añadido el DNI
                Pacientes.paciente_update(update_data)  # Llamada con el objeto
                return jsonify({'message': 'Paciente actualizado exitosamente'}), 200
            else:
                return jsonify({'error': 'Paciente no encontrado'}), 404
        else:
            return jsonify({'error': 'DNI del paciente es requerido'}), 400

    @classmethod
    @token_required
    def eliminar(cls, current_user):
        dni_paciente = request.args.get('dni_paciente')
        if dni_paciente:
            paciente = Pacientes.get_paciente(dni_paciente)
            if paciente:
                paciente_obj = Pacientes()
                paciente_obj.dni_paciente = dni_paciente
                Pacientes.paciente_delete(paciente_obj)
                return jsonify({'message': 'Paciente eliminado exitosamente'}), 200
            else:
                return jsonify({'error': 'Paciente no encontrado'}), 404
        else:
            return jsonify({'error': 'DNI del paciente es requerido'}), 400

    @classmethod
    @token_required
    def cerrar_sesion(cls, current_user):
        return jsonify({'message': 'Sesión cerrada exitosamente'}), 200
