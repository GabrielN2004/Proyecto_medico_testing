import pytest
import datetime
from mysql.connector.errors import IntegrityError, DataError, Error
from ..repository.profesional_repo import ProfesionalRepository
from config import TestingConfig
from app.database import DatabaseConnection
from ..models.profesional_models import Profesional
from ..tests.util import cleanup

@pytest.fixture
def config():
    return DatabaseConnection(TestingConfig)

@pytest.fixture
def profesional_repository(config):
    return ProfesionalRepository(config)

@pytest.fixture(autouse=True)
def setup(config):
    db = config

    with db.get_connection() as conn:
        cursor = conn.cursor()
        with open("datos_de_la_db.sql", "r") as file:
            sql_script = file.read()

        sql_statements = sql_script.split(";")

        for statement in sql_statements:
            if statement.strip():
                cursor.execute(statement)

        conn.commit()
        cursor.close()

    yield  # Permite ejecutar las pruebas

    with db.get_connection() as conn:
        cleanup(conn)

# Test para obtener un profesional por ID
def test_get_professional_by_id(profesional_repository):
    # Arrange
    profesional_id = 1
    
    # Act
    profesional = profesional_repository.get_professional_by_id(profesional_id)
    
    # Assert
    assert profesional is not None
    assert profesional["id_profesional"] == profesional_id

# Test para obtener un profesional por ID que no existe
def test_get_professional_by_id_not_found(profesional_repository):
    # Arrange
    profesional_id = 9999  # ID inexistente
    
    # Act
    profesional = profesional_repository.get_professional_by_id(profesional_id)
    
    # Assert
    assert profesional is None

# Test para obtener profesionales por especialidad
def test_get_profesionales_by_idespecialidad(profesional_repository):
    # Arrange
    especialidad_id = 2
    
    # Act
    profesionales = profesional_repository.get_profesionales_by_idespecialidad(especialidad_id)
    
    # Assert
    assert isinstance(profesionales, list)
    assert all(prof["id_especialidad"] == especialidad_id for prof in profesionales)

# Test para obtener profesionales por especialidad inexistente
def test_get_profesionales_by_idespecialidad_not_found(profesional_repository):
    # Arrange
    especialidad_id = 9999  # ID inexistente
    
    # Act
    profesionales = profesional_repository.get_profesionales_by_idespecialidad(especialidad_id)
    
    # Assert
    assert profesionales == []

# Test para obtener un profesional por email
def test_get_profesionales_by_email(profesional_repository):
    # Arrange
    email = "test@correo.com"
    
    # Act
    profesional = profesional_repository.get_profesionales_by_email(email)
    
    # Assert
    assert profesional is not None
    assert profesional["profesional_email"] == email

# Test para obtener un profesional por email inexistente
def test_get_profesionales_by_email_not_found(profesional_repository):
    # Arrange
    email = "noexiste@correo.com"
    
    # Act
    profesional = profesional_repository.get_profesionales_by_email(email)
    
    # Assert
    assert profesional is None
