from ..database import DatabaseConnection
from datetime import datetime

class Turnos:
    def __init__(self, id_turno=None, dni_paciente=None, id_especialidad=None, id_profesional=None, id_obrasocial=None, fecha_turno=None, id_horario=None):
        self.id_turno = id_turno
        self.dni_paciente = dni_paciente
        self.id_especialidad = id_especialidad
        self.id_profesional = id_profesional
        self.id_obrasocial = id_obrasocial
        self.fecha_turno = fecha_turno
        self.id_horario = id_horario

    def serialize(self):
        """
        Serializa la instancia del objeto Turnos en un diccionario.
        """
        return {
        'id_turno': self.id_turno,
        'dni_paciente': self.dni_paciente,
        'id_especialidad': self.id_especialidad,
        'id_profesional': self.id_profesional,
        'id_obrasocial': self.id_obrasocial,
        'fecha_turno': self.fecha_turno,
        'id_horario': self.id_horario
    }

    @classmethod
    def get_all_turnos(cls):
        """
        Obtiene todos los turnos.
        """
        query = """SELECT * FROM turnos"""
        results = DatabaseConnection.fetch_all(query)
        if results:
            turnos = [cls(*result).serialize() for result in results]
            return turnos
        return []

    @classmethod
    def get_turnos_by_paciente(cls, dni_paciente):
        """
        Obtiene todos los turnos de un paciente específico con datos descriptivos.
        """
        query = """
            SELECT 
                t.id_turno,
                t.dni_paciente,
                t.fecha_turno,
                h.horario_num,
                e.especialidad_name AS especialidad,
                p.profesional_fullname AS profesional,
                os.obrasocial_name AS obrasocial
            FROM db_centro_medico_1.turnos t
            JOIN db_centro_medico_1.horarios h ON t.id_horario = h.id_horario
            JOIN db_centro_medico_1.especialidades e ON t.id_especialidad = e.id_especialidad
            JOIN db_centro_medico_1.profesionales p ON t.id_profesional = p.id_profesional
            JOIN db_centro_medico_1.obrasociales os ON t.id_obrasocial = os.id_obrasocial
            WHERE t.dni_paciente = %s
        """
        params = (dni_paciente, )
        results = DatabaseConnection.fetch_all(query, params)
        
        if results:
            # Devuelve los resultados como una lista de diccionarios (puedes personalizar el formato según sea necesario)
            turnos = [
                {
                    "id_turno": result[0],
                    "dni_paciente": result[1],
                    "fecha_turno": datetime.strftime(result[2], "%d/%m/%Y"),
                    "horario": result[3],
                    "especialidad": result[4],
                    "profesional": result[5],
                    "obrasocial": result[6],
                }
                for result in results
            ]
            return turnos
        return []

    @classmethod
    def create_turno(cls, turno):
        """
        Crea un nuevo turno.
        """
        query = """INSERT INTO db_centro_medico_1.turnos (dni_paciente, id_especialidad, id_profesional, id_obrasocial, fecha_turno, id_horario)
                VALUES (%s, %s, %s, %s, %s, %s)"""
        params = (turno.dni_paciente, turno.id_especialidad, turno.id_profesional, turno.id_obrasocial, turno.fecha_turno, turno.id_horario)
        
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete_turno(cls, id_turno):
        """
        Elimina un turno por su ID.
        """
        query = """DELETE FROM turnos WHERE id_turno = %s"""
        params = (id_turno, )
        try:
            DatabaseConnection.execute_query(query, params)
            return True
        except Exception as e:
            print(f"Error deleting turno: {e}")
            return False


class Especialidades:

    def __init__(self, id_especialidad=None, especialidad_name=None):
        self.id_especialidad = id_especialidad
        self.especialidad_name = especialidad_name

    def serialize(self):
        return {
            "id_especialidad": self.id_especialidad,
            "especialidad_name": self.especialidad_name
        }
    
    @classmethod
    def get_especialidad_all(cls):
        query = """SELECT * FROM db_centro_medico_1.especialidades"""
        results = DatabaseConnection.fetch_all(query)
        if results:
            especialidades = [cls(*result) for result in results]
            return especialidades
        return 

class Profesionales:
    def __init__(self, id_profesional= None,
                profesional_fullname= None,
                profesional_matricula= None,
                profesional_email= None,
                profesional_password= None,
                id_especialidad= None):
        
        self.id_profesional= id_profesional
        self.profesional_fullname= profesional_fullname
        self.profesional_matricula= profesional_matricula
        self.profesional_email= profesional_email
        self.profesional_password= profesional_password
        self.id_especialidad=id_especialidad

    def serialize(self):
        return{
            "id_profesional": self.id_profesional,
            "profesional_fullname": self.profesional_fullname,
            "profesional_matricula": self.profesional_matricula,
            "profesional_email": self.profesional_email,
            "profesional_password": self.profesional_password,
            "id_especialidad": self.id_profesional
        }
    
    @classmethod
    def get_profesionales_by_idespecialidad(cls, id_especialidad):
        query = """SELECT * from  db_centro_medico_1.profesionales where id_especialidad = %s"""
        params = (id_especialidad, )
        results = DatabaseConnection.fetch_all(query, params=params)
        if results:
            profesionales = [cls(*result).serialize() for result in results]
            return profesionales
        return []
    
class Obrasocial:
    def __init__(self, id_obrasocial = None, obrasocial_name= None):
        self.id_obrasocial=id_obrasocial
        self.obrasocial_name = obrasocial_name

    def serialize(self):
        return{
            "id_obrasocial":self.id_obrasocial,
            "obrasocial_name":self.obrasocial_name
        }
    @classmethod
    def get_obrasocial_by_profesional(cls, id_profesional):
        query = """SELECT obrasociales.id_obrasocial, obrasociales.obrasocial_name 
                FROM db_centro_medico_1.obrasociales 
                JOIN db_centro_medico_1.profesional_obrasocial 
                ON obrasociales.id_obrasocial = profesional_obrasocial.id_obrasocial 
                WHERE profesional_obrasocial.id_profesional = %s"""
        params = (id_profesional,)
        results = DatabaseConnection.fetch_all(query, params)
        if results:
            obrasociales = [cls(result[0], result[1]).serialize() for result in results]
            return obrasociales
        return []

class HorarioTurno:
    def __init__(self, id_horario = None , horario_num = None):
        self.id_horario = id_horario
        self.horario_num = horario_num

    def serialize(self):
        return{
            "id_horario": self.id_horario,
            "horario_num": self.horario_num
        }
    
    @classmethod
    def get_horario_by_idprofesional(cls, id_profesional):
        query = """SELECT horarios.id_horario, horarios.horario_num FROM db_centro_medico_1.horarios
                JOIN db_centro_medico_1.horario_profesional 
                ON horarios.id_horario = horario_profesional.id_horario
                WHERE horario_profesional.id_profesional = %s"""
        params = (id_profesional,)
        results = DatabaseConnection.fetch_all(query, params)
        if results:
            horarios = [cls(result[0], result[1]).serialize() for result in results]
            return horarios
        return []
    
    @classmethod
    def get_idhorario(cls, id_profesional):
        query = """SELECT horarios.id_horario 
                FROM db_centro_medico_1.horarios 
                JOIN db_centro_medico_1.horario_profesional 
                ON horarios.id_horario = horario_profesional.id_horario
                WHERE horario_profesional.id_profesional = %s"""
        params = (id_profesional,)
        results = DatabaseConnection.fetch_all(query, params)
        if results:
            horarios = [result[0] for result in results]  # Solo extraer el id_horario
            return horarios
        return []