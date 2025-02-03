from ..database import DatabaseConnection

class Profesional:
    def __init__(self, id_profesional=None, profesional_fullname=None, profesional_matricula=None, 
                    profesional_email=None, profesional_password=None, id_especialidad=None):
        self.id_profesional = id_profesional
        self.profesional_fullname = profesional_fullname
        self.profesional_matricula = profesional_matricula
        self.profesional_email = profesional_email
        self.profesional_password = profesional_password
        self.id_especialidad = id_especialidad

    def serialize(self):
        return {
            "id_profesional": self.id_profesional,
            "profesional_fullname": self.profesional_fullname,
            "profesional_matricula": self.profesional_matricula,
            "profesional_email": self.profesional_email,
            "profesional_password": self.profesional_password,
            "id_especialidad": self.id_especialidad
        }

    @classmethod
    def get_profesional(cls, id_profesional):
        """Obtiene los datos de un profesional por su ID"""
        query = """SELECT * FROM db_centro_medico_1.profesionales WHERE id_profesional = %s;"""
        params = (id_profesional,)
        result = DatabaseConnection.fetch_one(query, params)
        return result

    @classmethod
    def update_profesional(cls, profesional):
        """Actualiza los datos de un profesional"""
        query = """UPDATE db_centro_medico_1.profesionales 
                SET profesional_fullname = %s, profesional_matricula = %s, profesional_email = %s, 
                    profesional_password = %s, id_especialidad = %s 
                    WHERE id_profesional = %s;"""
        params = (profesional.profesional_fullname, profesional.profesional_matricula, profesional.profesional_email,
                    profesional.profesional_password, profesional.id_especialidad, profesional.id_profesional)
        DatabaseConnection.execute_query(query, params)
        return None

    @classmethod
    def delete_profesional(cls, profesional):
        """Elimina un profesional por ID"""
        query = "DELETE FROM db_centro_medico_1.profesionales WHERE id_profesional = %s;"
        params = (profesional.id_profesional,)
        DatabaseConnection.execute_query(query, params)
        return {'message': 'Profesional eliminado con éxito'}, 204

    @classmethod
    def get_profesional_by_email(cls, profesional_email):
        """Obtiene un profesional por su email."""
        query = "SELECT * FROM Profesional WHERE email = %s"
        params = (profesional_email, )
        DatabaseConnection.fetch_one(query, params)

    @classmethod
    def get_turnos_by_profesional(cls, dni_profesional):
        """
        Obtiene todos los turnos de un profesional específico con datos descriptivos.
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
            WHERE t.id_profesional = %s
        """
        params = (dni_profesional, )
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
