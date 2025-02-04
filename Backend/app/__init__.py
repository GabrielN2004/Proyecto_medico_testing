import os
from flask import Flask
from config import *
from dotenv import load_dotenv
from flask_cors import CORS  # Importar CORS
from app.database import DatabaseConnection
from .Routes.authcontext_bp import auth_bp
from .Routes.paciente_bp import paciente_bp
from .Routes.user_bp import user_bp
from .Routes.turnos_bp import turno_bp
from .Routes.profile_bp import profile_bp

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def create_app():
    """Crear la aplicación Flask y configurarla."""
    # Crear una instancia de la aplicación Flask
    app = Flask(__name__)

    # Habilitar CORS para todas las rutas (si necesitas configuraciones específicas, ajusta los parámetros)
    CORS(app, supports_credentials=True)

    # Load the configuration
    env = os.getenv("FLASK_ENV", "development").lower()

    app.logger.info("Running in %s environment", env)

    class_Config ={
        "Development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }.get(env, DevelopmentConfig)
    
    app.config.from_object(class_Config)
    # Conectar a la base de datos (esto puede ser llamado desde donde se necesite)
    DatabaseConnection.get_connection()

    # Configurar las rutas
    app.register_blueprint(auth_bp)
    app.register_blueprint(paciente_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(turno_bp)
    app.register_blueprint(profile_bp)
    return app
