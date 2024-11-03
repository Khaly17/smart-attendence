import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'db-password')
    POSTGRES_DB = os.getenv('POSTGRES_DB', 'smart_attendance_db')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')

    # URI de la base de données PostgreSQL
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}'
        f'@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    )

    URI = "postgresql://uce6kgae6q68vb:p730fd6dd54cc326d92bdcabce6fe9e8dfc8b636d4916fd1331b8f54b6f3447f4@cd27da2sn4hj7h.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d16ap676eq1da9"
    SQLALCHEMY_DATABASE_URI = (URI)

    # Configuration du broker MQTT
    MQTT_BROKER_URL = os.getenv('MQTT_BROKER_URL', 'test.mosquitto.org')
    MQTT_BROKER_PORT = int(os.getenv('MQTT_BROKER_PORT', 1883))  # Port du broker MQTT
    MQTT_USERNAME = os.getenv('MQTT_USERNAME', '')  # Si un nom d'utilisateur est requis
    MQTT_PASSWORD = os.getenv('MQTT_PASSWORD', '')  # Si un mot de passe est requis
    MQTT_KEEPALIVE = int(os.getenv('MQTT_KEEPALIVE', 60))  # Intervalle keep-alive
    MQTT_TLS_ENABLED = os.getenv('MQTT_TLS_ENABLED', 'False').lower() in ['true', '1']

    DEBUG = os.getenv('DEBUG', 'True').lower() in ['true', '1']
