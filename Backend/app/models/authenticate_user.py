from app.database import DatabaseConnection  # Asumiendo que ya tienes esta clase para interactuar con la DB

class AuthenticateUser:
    @classmethod
    def authenticate_user(cls, email, password):
        """Autentica al usuario, valida el email y la contraseña, y obtiene el rol del usuario."""
        
        # Consulta SQL para obtener el ID de usuario y el id_role basados en el correo electrónico
        query = """
            SELECT u.id_usuario, u.usuario_password, u.id_role, r.role_name
            FROM usuarios u
            JOIN roles r ON u.id_role = r.id_role
            WHERE u.usuario_email = %s
        """
        
        # Ejecutar la consulta y obtener el resultado
        result = DatabaseConnection.fetch_one(query, (email,))

        if not result:
            return None  # El usuario no existe
        
        id_usuario, usuario_password, id_role, role_name = result

        # Verificar si la contraseña proporcionada coincide con la almacenada
        if password != usuario_password:
            return None  # Contraseña incorrecta
        
        # Si todo es correcto, devolver el user_id y el rol
        return {'id_usuario': id_usuario, 'role_name': role_name, 'id_role': id_role}

