from ..models.paciente_models import Pacientes
from flask import request, jsonify 

class PacienteController:
    """Clase controller de paciente"""

    @classmethod
    def create_paciente(cls):
        """Se crea un paciente"""
        # Usar request.json.get() en lugar de request.args.get()
        paciente = Pacientes(
            dni_paciente=request.json.get('dni_paciente', ''),
            paciente_name=request.json.get('paciente_name', ''),
            paciente_lastname=request.json.get('paciente_lastname', ''),
            paciente_email=request.json.get('paciente_email', ''),
            paciente_password=request.json.get('paciente_password', ''),
            id_obrasocial=request.json.get('id_obrasocial', '')
        )

        # Guardar el paciente en la base de datos
        Pacientes.paciente_create(paciente)
        
        # Respuesta exitosa
        return jsonify({'message': 'Paciente creado exitosamente'}), 201
    
        