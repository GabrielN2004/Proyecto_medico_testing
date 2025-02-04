def cleanup(conn):
    """Fixture para limpiar la base de datos y resetear ids."""
    with conn.cursor() as cursor:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        # Reset table users
        cursor.execute("TRUNCATE TABLE usuario;")
        cursor.execute("ALTER TABLE usuario AUTO_INCREMENT = 1;")
        # Reset table students
        cursor.execute("TRUNCATE TABLE profesionales;")
        cursor.execute("ALTER TABLE profesionales AUTO_INCREMENT = 1;")
        # Reset table professors
        cursor.execute("TRUNCATE TABLE especialidades;")
        cursor.execute("ALTER TABLE especialidades AUTO_INCREMENT = 1;")
        # Reset table activities
        #cursor.execute("TRUNCATE TABLE activities;")
        #cursor.execute("ALTER TABLE activities AUTO_INCREMENT = 1;")
        # Reset table projects
        #cursor.execute("TRUNCATE TABLE projects;")
        #cursor.execute("ALTER TABLE projects AUTO_INCREMENT = 1;")
        # Reset table members
        #cursor.execute("TRUNCATE TABLE members;")
        #cursor.execute("ALTER TABLE members AUTO_INCREMENT = 1;")

        conn.commit()

        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        conn.commit()
        