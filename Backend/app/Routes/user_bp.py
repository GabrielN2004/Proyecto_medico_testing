from flask import Blueprint
from ..controllers.user_controllers import UsuarioController

user_bp = Blueprint('user_bp', __name__)


user_bp.route('/usuario', methods=['POST'])(UsuarioController.create_usuario)
user_bp.route('/usuario/get_token', methods=['POST'])(UsuarioController.get_token_usuario)
