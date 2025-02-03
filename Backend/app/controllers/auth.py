import jwt
import datetime
import os
from dotenv import load_dotenv
from flask import current_app

# Cargar variables del archivo .env
load_dotenv(override=True)  

class Auth:
    @staticmethod
    def encode_auth_token(id_usuario, role_name):
        """Genera un token de autenticación con el ID del usuario y su rol."""
        try:
            expiration_time = os.getenv("JWT_EXPIRATION_TIME", "3600").strip()  # Eliminar espacios extras
            expiration_time = int(expiration_time)  # Convertir a número

            payload = {
                        'id_usuario': id_usuario,  # Esto debería estar bien
                        'role_name': role_name,  # Este también debe estar presente
                        'iat': datetime.datetime.utcnow(),
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expiration_time)
                    }

            
            secret_key = current_app.config.get('SECRET_KEY', os.getenv('JWT_SECRET_KEY'))
            algorithm = current_app.config.get('JWT_ALGORITHM', 'HS256')

            return jwt.encode(payload, secret_key, algorithm=algorithm)
        except ValueError:
            print("⚠️ Advertencia: JWT_EXPIRATION_TIME no es un número válido. Usando 3600 segundos por defecto.")
            expiration_time = 3600  # Valor por defecto
        except Exception as e:
            print(f"❌ Error al generar el token: {e}")
            return None

    @staticmethod
    def decode_auth_token(auth_token):
        """Decodifica un token de autenticación y devuelve el user_id y el rol."""
        try:
            secret_key = current_app.config.get('SECRET_KEY', os.getenv('JWT_SECRET_KEY'))
            algorithm = current_app.config.get('JWT_ALGORITHM', 'HS256')

            payload = jwt.decode(auth_token, secret_key, algorithms=[algorithm])
            return {'id_usuario': payload['id_usuario'], 'role_name': payload['role_name']}


        except jwt.ExpiredSignatureError:
            print("❌ El token ha expirado.")
            return None
        except jwt.InvalidTokenError:
            print("❌ Token inválido.")
            return None
        except Exception as e:
            print(f"❌ Error al decodificar el token: {e}")
            return None
