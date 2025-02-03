from ..database import DatabaseConnection

class Pacientes:
    """model de la clase Pacientes"""
    def __init__(self, dni_paciente=None,
                paciente_name=None,
                paciente_lastname=None,
                paciente_email=None,
                paciente_password=None,
                id_obrasocial=None):
        
        """metodo constructor"""
        self.dni_paciente= dni_paciente
        self.paciente_name= paciente_name
        self.paciente_lastname= paciente_lastname
        self.paciente_email= paciente_email
        self.paciente_password= paciente_password
        self.id_obrasocial= id_obrasocial

    def serialize(self):
        return {
            "dni_paciente": self.dni_paciente,
            "paciente_name": self.paciente_name,
            "paciente_lastname": self.paciente_lastname,
            "paciente_email": self.paciente_email,
            "paciente_password": self.paciente_password,
            "id_obrasocial": self.id_obrasocial,
        }
    
    @classmethod
    def paciente_create(cls,paciente):
        query= """INSERT INTO db_centro_medico_1.pacientes(dni_paciente, paciente_name, paciente_lastname, paciente_email, paciente_password, id_obrasocial) VALUES (%s,%s,%s,%s,%s,%s);"""
        params = (paciente.dni_paciente, paciente.paciente_name, paciente.paciente_lastname, paciente.paciente_email, paciente.paciente_password, paciente.id_obrasocial)
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def get_paciente_all(cls):
        """Obtiene todo los pacientes de la Database"""
        query = """SELECT * FROM db_centro_medico_1.pacientes """
        results = DatabaseConnection.fetch_all(query)

        pacientes = []

        if results is not None:
            for result in results:
                pacientes.append(cls(*result))
        return pacientes
    
    @classmethod
    def get_paciente(cls, dni_paciente):
        """Obtiene todos los datos del paciente filtrandolo por si DNI"""
        query = """SELECT * FROM db_centro_medico_1.pacientes where dni_paciente = %s;"""
        params = (dni_paciente, )
        result = DatabaseConnection.fetch_one(query,params)
        return result
    
    @classmethod
    def paciente_update(cls, paciente):
        query = "UPDATE db_centro_medico_1.pacientes SET paciente_name = %s, paciente_lastname = %s, paciente_email = %s, paciente_password = %s, id_obrasocial= %s WHERE dni_paciente = %s ;"
        params = (paciente.paciente_name, paciente.paciente_lastname, paciente.paciente_email, paciente.paciente_password, paciente.id_obrasocial,paciente.dni_paciente)
        DatabaseConnection.execute_query(query, params=params)
        return None
    
    @classmethod
    def paciente_delete(cls, paciente):
        query = "DELETE FROM db_centro_medico_1.pacientes WHERE dni_paciente = %s;"
        params = (paciente.dni_paciente,)
        DatabaseConnection.execute_query(query, params)
        return {'message': 'Paciente eliminado con exito'},204
    
    @classmethod
    def get_paciente_by_email(cls, paciente_email):
        """Obtiene un paciente por su email."""
        query = "SELECT * FROM Pacientes WHERE email = %s"
        params = (paciente_email,)
        DatabaseConnection.fetch_one(query, params)