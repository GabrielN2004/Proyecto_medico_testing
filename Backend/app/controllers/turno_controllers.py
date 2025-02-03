from ..models.turno_models import Turnos, Profesionales, Especialidades, HorarioTurno, Obrasocial
from ..models.user_models import Usuarios
from flask import request, jsonify
from functools import wraps
from..controllers.auth import Auth
import jwt
from datetime import datetime 

def verificar_token(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        token = None
        # Buscamos el token en el encabezado de la solicitud
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]  # Extraemos el token

        if not token:
            return jsonify({'message': 'Token no encontrado'}), 403

        try:
            # Decodificamos el token
            data = Auth.decode_auth_token(token)
            if data:
                current_user = data.get('id_usuario')  # Usamos .get() en vez de ['id_usuario']
                if not current_user:
                    return jsonify({'message': 'Token no contiene id_usuario'}), 401
            else:
                return jsonify({'message': 'Token inválido o expirado'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'El token ha expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token inválido'}), 401

        return f(current_user, *args, **kwargs)  # Pasamos el user_id a la función protegida

    return decorador

class TurnoController:
    @classmethod
    @verificar_token
    def get_all_turnos(cls, current_user):
        """
        Obtiene todos los turnos.
        """
        turnos = Turnos.get_all_turnos()
        return jsonify(turnos), 200

    @classmethod
    @verificar_token
    def get_turnos_by_paciente(cls, current_user, dni_paciente):
        """
        Obtiene todos los turnos de un paciente específico.
        """
        turnos = Turnos.get_turnos_by_paciente(dni_paciente)
        if turnos:
            return jsonify(turnos), 200
        return jsonify({"message": "No turnos found for this patient."}), 404


    @classmethod
    @verificar_token
    def create_turno(cls, current_user):
        """
        Crea un nuevo turno, verificando que el usuario esté autenticado.
        """
        try:
            data = request.get_json()
            dni_paciente = data['dni_paciente']
            id_especialidad = data['id_especialidad']
            id_profesional = data['id_profesional']
            id_obrasocial = data['id_obrasocial']
            fecha_turno = datetime.strptime(data['fecha_turno'], "%d/%m/%Y")
            id_horario = data['id_horario']
            
            nuevo_turno = Turnos(
                dni_paciente=dni_paciente,
                id_especialidad=id_especialidad,
                id_profesional=id_profesional,
                id_obrasocial=id_obrasocial,
                fecha_turno=fecha_turno,
                id_horario=id_horario
            )
            
            Turnos.create_turno(nuevo_turno)
            return jsonify({"message": "Turno created successfully."}), 201
        except Exception as e:
            return jsonify({"message": f"Error creating turno: {e}"}), 400

    @classmethod
    @verificar_token
    def delete_turno(cls, current_user, id_turno):
        """
        Elimina un turno por su ID, solo si el usuario está autenticado.
        """
        success = Turnos.delete_turno(id_turno)
        if success:
            return jsonify({"message": "Turno deleted successfully."}), 200
        return jsonify({"message": "Error deleting turno."}), 400


class EspecialidadControllers:

    @classmethod
    def get_especialidades_all(cls):
        try:
            especialidad_objects = Especialidades.get_especialidad_all()
            especialidades = [especialidad.serialize() for especialidad in especialidad_objects]
            return especialidades, 200
        except Exception as e:
            print(f"Error: {e}")
            return {'message': 'Internal Server Error'}, 500

class ProfesionalControllers:
    @classmethod
    def get_profesional_by_id_especialidad(cls, id_especialidad):
        try:
            profesional = Profesionales.get_profesionales_by_idespecialidad(id_especialidad)
            if profesional:
                return jsonify(profesional), 200
            else:
                return {'message': 'Profesional No Encontrado'}, 404
        except Exception as e:
            print(f"Error: {e}")
            return {'message': 'Internal Server Error'}, 500

class ObrasocialesControllers:

    @classmethod
    def get_obrasocial_by_idprofesional(cls, id_profesional):
        try:
            obrasocial = Obrasocial.get_obrasocial_by_profesional(id_profesional)
            if obrasocial:
                return jsonify(obrasocial), 200
            else:
                return {'message': 'Obra social no encontrada'}, 404
        except Exception as e:
            print(f"Error: {e}")
            return {'message': 'Internal Server Error'}, 500

class HorariosTurnoControllers:
    @classmethod
    def get_horarioturno_by_idprofesional(cls, id_profesional):
            try:
                horario = HorarioTurno.get_horario_by_idprofesional(id_profesional)
                if horario:
                    return jsonify(horario), 200
                else:
                    return {'message': 'Horario no encontrado'}, 404
            except Exception as e:
                print(f"Error: {e}")
                return {'message': 'Internal Server Error'}, 500
            
    @classmethod
    def get_id_horarios(id_profesional):
        try:
            # Llamar al método de la clase HorarioTurno para obtener solo los IDs de horarios
            horarios_ids = HorarioTurno.get_idhorario(id_profesional)
            if horarios_ids:
                return jsonify(horarios_ids), 200  # Retornar los IDs en formato JSON
            else:
                return jsonify({"message": "No se encontraron IDs de horarios para este profesional"}), 404
        except Exception as e:
            # Manejo de errores
            return jsonify({"message": f"Error: {str(e)}"}), 500