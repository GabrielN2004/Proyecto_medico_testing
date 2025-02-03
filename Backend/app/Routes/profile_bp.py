from flask import Blueprint
from ..controllers.profile_controllers import ProfilePaciente

profile_bp = Blueprint('profile_bp', __name__)

# Ruta para obtener el perfil del paciente
profile_bp.route('/user/profile', methods=['GET'])(ProfilePaciente.profilepaciente)

# Ruta para modificar los datos del paciente
profile_bp.route('/user/modificar', methods=['PUT'])(ProfilePaciente.modificar)

# Ruta para eliminar un paciente
profile_bp.route('/user/eliminar', methods=['DELETE'])(ProfilePaciente.eliminar)

# Ruta para cerrar sesión
profile_bp.route('/user/cerrar_sesion', methods=['POST'])(ProfilePaciente.cerrar_sesion)
