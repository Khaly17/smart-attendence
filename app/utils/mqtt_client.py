# app/utils/mqtt_client.py
import paho.mqtt.client as mqtt
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    """Callback lors de la connexion réussie au broker MQTT."""
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe('attendance/topic')  # S'abonner au topic
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, message):
    """Callback exécuté lors de la réception d'un message sur le topic MQTT."""
    app = userdata['app']  # Récupérer l'instance de l'application Flask depuis 'userdata'
    
    with app.app_context():  # Utiliser l'objet app pour créer le contexte
        badge_id = message.payload.decode()
        print(f"Message reçu avec badge_id: {badge_id}")

        # Importer les modèles et la base de données ici
        from app.models.user import User
        from app.models.attendance import Attendance
        from app import db

        # Rechercher l'utilisateur dans la base de données
        user = User.query.filter_by(badge_id=badge_id).first()

        if user:
            # Enregistrer la présence
            new_attendance = Attendance(user_id=user.id)
            db.session.add(new_attendance)
            db.session.commit()
            print(f"Attendance logged for user: {user.name} at {new_attendance.timestamp}")
        else:
            print(f"No user found with badge_id: {badge_id}")

def start_mqtt_client(app):
    """Démarrer le client MQTT et se connecter au broker."""
    client = mqtt.Client(userdata={'app': app})  # Passer l'instance de l'app via userdata
    client.on_connect = on_connect
    client.on_message = on_message

    # Connexion au broker MQTT
    mqtt_broker_url = 'test.mosquitto.org'
    mqtt_broker_port = 1883

    client.connect(mqtt_broker_url, mqtt_broker_port, 60)

    # Démarrer la boucle d'écoute des messages
    client.loop_start()
