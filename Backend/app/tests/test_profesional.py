import pytest

import datetime

from mysql.connector.errors import IntegrityError, DataError, Error
from ..repository.profesional_repo import ProfesionalRepository
from config import TestingConfig
from ..database import DatabaseConnection
from ..models.profesional_models import Profesional
from ..tests.util import cleanup


@pytest.fixture
def config():
    db = DatabaseConnection(TestingConfig)

    return db


@pytest.fixture
def activity_repository(config):
    db = config
    return ProfesionalRepository(db)


@pytest.fixture(autouse=True)
def setup(config):
    db = config

    with db.get_connection() as conn:
        cursor = conn.cursor()

        with open("db_centro_medico_test", "r") as file:
            sql_script = file.read()

        sql_statements = sql_script.split(";")

        for statement in sql_statements:
            if statement.strip():
                cursor.execute(statement)

        conn.commit()

        cursor.close()

    yield

    db = config
    with db.get_connection() as conn:
        cleanup(conn)

    def test_update_all_fields_success(profesional_repository):
        original_profesional = profesional_repository.get_professional_by_id(1)
        profesional = Profesional(
            id_profesional=1,
            profesional_fullname="Nombre Actualizado",
            profesional_matricula="123456",
            profesional_email="nuevo_email@example.com",
            profesional_password="nueva_clave",
            especialidad_id=2
        )
        profesional_repository.update_professional(profesional)
        updated_profesional = profesional_repository.get_professional_by_id(1)
        assert updated_profesional.profesional_fullname == "Nombre Actualizado"
        assert updated_profesional.profesional_matricula == "123456"
        assert updated_profesional.profesional_email == "nuevo_email@example.com"
        assert updated_profesional.profesional_password == "nueva_clave"
        assert updated_profesional.especialidad_id == 2

    def test_update_partial_fields(profesional_repository):
        original_profesional = profesional_repository.get_professional_by_id(1)
        profesional = Profesional(
            id_profesional=1,
            profesional_fullname="Nuevo Parcial",
            profesional_matricula=original_profesional.profesional_matricula,
            profesional_email=original_profesional.profesional_email,
            profesional_password=original_profesional.profesional_password,
            especialidad_id=original_profesional.especialidad_id
        )
        profesional_repository.update_professional(profesional)
        updated_profesional = profesional_repository.get_professional_by_id(1)
        assert updated_profesional.profesional_fullname == "Nuevo Parcial"
        assert updated_profesional.profesional_matricula == original_profesional.profesional_matricula

    def test_update_with_invalid_email(profesional_repository):
        profesional = Profesional(
            id_profesional=1,
            profesional_fullname="Nombre",
            profesional_matricula="123456",
            profesional_email="email_invalido",
            profesional_password="clave",
            especialidad_id=1
        )
        with pytest.raises(DataError):
            profesional_repository.update_professional(profesional)

    def test_update_notexistent_profesional(profesional_repository):
        profesional = Profesional(
            id_profesional=9999,
            profesional_fullname="No Existente",
            profesional_matricula="000000",
            profesional_email="noexistente@example.com",
            profesional_password="clave",
            especialidad_id=1
        )
        profesional_repository.update_professional(profesional)
        notexistent_profesional = profesional_repository.get_professional_by_id(9999)
        assert notexistent_profesional is None

    def test_delete_existing_profesional(profesional_repository):
        profesional_id = 1
        profesional_repository.delete_professional(profesional_id)
        profesional = profesional_repository.get_professional_by_id(profesional_id)
        assert profesional is None

    def test_delete_non_existing_profesional(profesional_repository):
        profesional_id = 9999
        profesional_repository.delete_professional(profesional_id)
        profesional = profesional_repository.get_professional_by_id(profesional_id)
        assert profesional is None

    def test_delete_non_valid_profesional_id(profesional_repository):
        with pytest.raises(Error):
            profesional_repository.delete_professional("invalid_id")
