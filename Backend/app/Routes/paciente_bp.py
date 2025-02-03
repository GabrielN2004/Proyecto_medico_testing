from flask import Blueprint

from ..controllers.paciente_controllers import PacienteController

paciente_bp = Blueprint('paciente_bp', __name__)

paciente_bp.route('/pacientes', methods=['POST'])(PacienteController.create_paciente)