from ..database import DatabaseConnection

class Usuarios:
    """Clase usuario"""

    def __init__(self, id_usuario = None, usuario_email=None, usuario_password=None, id_role=None):
        """Método constructor"""
        self.id_usuario = id_usuario
        self.usuario_email = usuario_email
        self.usuario_password = usuario_password
        self.id_role = id_role

    def serialize(self):
        """Método para convertir el objeto usuario a un formato serializable"""
        return {
            "id_usuario": self.id_usuario,
            "usuario_email": self.usuario_email,
            "usuario_password": self.usuario_password,
            "id_role": self.id_role,
        }

    @classmethod
    def usuario_create(cls, usuario):
        """Crea un nuevo usuario en la base de datos"""
        query = """INSERT INTO db_centro_medico_1.usuarios(usuario_email, usuario_password, id_role) VALUES (%s,%s,%s);"""
        params = (usuario.usuario_email, usuario.usuario_password, usuario.id_role)
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def get_by_id(cls, id_usuario):
        """Obtiene un usuario por su ID"""
        query = """SELECT * FROM db_centro_medico_1.usuarios WHERE id_usuario = %s;"""
        params = (id_usuario, )
        result = DatabaseConnection.execute_query(query, params=params)
        print(result)
        # Asegúrate de que result contiene un único elemento
        if result:
            # Si la consulta devuelve solo un resultado, accede al primer elemento
            user_data = result[0]  # Asegúrate de que 'result' es una lista o tupla
            return cls(
                    id_usuario=id_usuario,
                    usuario_email=user_data['usuario_email'],
                    usuario_password=user_data['usuario_password'],
                    id_role=user_data['id_role'])
        return None

    @classmethod
    def get_by_email(cls, usuario_email):
        """Obtiene un usuario por su email"""
        query = """SELECT usuario_email, usuario_password, id_role 
                FROM db_centro_medico_1.usuarios 
                WHERE usuario_email = %s;"""
        params = (usuario_email, )
        result = DatabaseConnection.fetch_one(query, params)
        
        if result:
            return cls(usuario_email=result['usuario_email'], 
                    usuario_password=result['usuario_password'],
                    id_role=result['id_role'])
        return None

    @classmethod
    def update_usuario(cls, usuario_id, new_email=None, new_password=None, new_role=None):
        """Actualiza los datos de un usuario"""
        query = """UPDATE db_centro_medico_1.usuarios 
                SET usuario_email = %s, usuario_password = %s, id_role = %s 
                WHERE id_usuario = %s;"""
        params = (new_email, new_password, new_role, usuario_id)
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete_usuario(cls, usuario_id):
        """Elimina un usuario por su ID"""
        query = """DELETE FROM db_centro_medico_1.usuarios WHERE id_usuario = %s;"""
        params = (usuario_id,)
        DatabaseConnection.execute_query(query, params=params)


