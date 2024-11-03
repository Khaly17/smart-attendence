# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.utils.mqtt_client import start_mqtt_client
from flask_cors import CORS 

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialiser SQLAlchemy et Migrate
    db.init_app(app)
    migrate.init_app(app, db)


    # CORS(app, resources={r"/*": {"origins": "http://localhost:4200,https://smart-attendence-esge.web.app/"}})
    CORS(app, resources={r"/*": {"origins": ["http://localhost:4200", "https://smart-attendence-esge.web.app"]}})

    # Importer les modèles après l'initialisation de l'application
    from app.models import user, attendance

    # Enregistrer les routes
    from app.routes import user_routes, attendance_routes
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(attendance_routes.bp)

    # Démarrer le client MQTT avec l'application Flask
    start_mqtt_client(app)

    return app
