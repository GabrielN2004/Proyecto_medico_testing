from flask import Blueprint
from ..controllers.authcontext import AuthContext

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/auth/login', methods = ['POST'])(AuthContext.login)
auth_bp.route('/auth/protegido', methods = ['GET'])(AuthContext.protected)