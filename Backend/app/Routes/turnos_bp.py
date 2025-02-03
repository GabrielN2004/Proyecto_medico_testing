from flask import Blueprint
from ..controllers.turno_controllers import TurnoController, EspecialidadControllers, ObrasocialesControllers, HorariosTurnoControllers, ProfesionalControllers

turno_bp = Blueprint('turno_bp', __name__)

turno_bp.route('/turno/obetener_turnos', methods=['GET'])(TurnoController.get_all_turnos)
turno_bp.route('/turno/turno_paciente/<int:dni_paciente>', methods=['GET'])(TurnoController.get_turnos_by_paciente)
turno_bp.route('/turno/reserva_turno', methods=['POST'])(TurnoController.create_turno)
turno_bp.route('/turno/eliminar_turno/<int:id_turno>', methods=['DELETE'])(TurnoController.delete_turno)

turno_bp.route('/turno/especialidad', methods=['GET'])(EspecialidadControllers.get_especialidades_all)
turno_bp.route('/turno/profesional/<int:id_especialidad>', methods=['GET'])(ProfesionalControllers.get_profesional_by_id_especialidad)
turno_bp.route('/turno/obrasocial/<int:id_profesional>', methods=['GET'])(ObrasocialesControllers.get_obrasocial_by_idprofesional)
turno_bp.route('/turno/horario', methods=['GET'])(HorariosTurnoControllers.get_id_horarios)
turno_bp.route('/turno/horario_profesional/<int:id_profesional>', methods=['GET'])(HorariosTurnoControllers.get_horarioturno_by_idprofesional)