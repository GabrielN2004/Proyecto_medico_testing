from ..database import DatabaseConnection
from flask import jsonify
class ProfesionalRepository(DatabaseConnection):
    def __init__(self, db: DatabaseConnection):
            self.db = db

    def get_all_professionals(self):
          query = """SELECT * FROM db_centro_medico_test.profesionales"""
          result = self.db.fetch_all(query)
          return result
    
    def get_professional_by_id(self, id_profesional):
            query = """SELECT * FROM db_centro_medico_test.profesionales WHERE id_profesional = %s"""
            params = (id_profesional,)
            result = self.db.fetch_one(query, params)
            return result
    
    def update_professional(self, profesional):
            query = """UPDATE db_centro_medico_test.profesionales SET profesional_fullname = %s, profesional_matricula = %s, profesional_email = %s, profesional_password = %s, especialidad_id = %s WHERE id_profesional = %s"""
            params = (profesional.profesional_fullname, profesional.profesional_matricula, profesional.profesional_email, profesional.profesional_password, profesional.especialidad_id, profesional.id_profesional)
            self.db.execute_query(query, params)
            return True
    
    def delete_professional(self, id_profesional):
            query = """DELETE FROM db_centro_medico_test.profesionales WHERE id_profesional = %s"""
            params = (id_profesional,)
            self.db.execute_query(query, params)
            return True
    
    def get_profesionales_by_idespecialidad(cls, id_especialidad):
        query = """SELECT * from  db_centro_medico_test.profesionales where id_especialidad = %s"""
        params = (id_especialidad, )
        results = DatabaseConnection.fetch_all(query, params=params)
        if results:
            profesionales = [cls(*result).serialize() for result in results]
            return profesionales
        return []
    
    def get_profesionales_by_email(cls, email):
          query = """SELECT * FROM db_centro_medico_test.profesionales WHERE profesional_email = %s"""
          params = (email,)
          result = DatabaseConnection.fetch_one(query, params)
          return result
    

