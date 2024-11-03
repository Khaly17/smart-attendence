# app/utils/mqtt_client.py
import paho.mqtt.client as mqtt
from datetime import datetime, time
from sqlalchemy import and_

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
            # Vérifier la dernière entrée de présence de l'utilisateur sans sortie pour aujourd'hui
            today = datetime.now().date()
            latest_entry = Attendance.query.filter(
                and_(
                    Attendance.user_id == user.id,
                    Attendance.entry_time != None,
                    Attendance.exit_time == None,
                    Attendance.entry_time >= datetime(today.year, today.month, today.day)
                )
            ).order_by(Attendance.entry_time.desc()).first()

            if latest_entry:
                # Si une entrée sans sortie existe, c'est une sortie
                latest_entry.exit_time = datetime.now()
                latest_entry.event_type = 'exit'
                print(f"Exit time logged for user: {user.name} at {latest_entry.exit_time}")
            else:
                current_time = datetime.now().time()
                status = "Present"
                if current_time > time(4, 0):  # Si l'heure est après 8:00 AM
                    status = "En Retard"
                # Sinon, c'est une nouvelle entrée
                new_attendance = Attendance(user_id=user.id, entry_time=datetime.now(), status=status, event_type="entry")
                db.session.add(new_attendance)
                print(f"Entry time logged for user: {user.name} at {new_attendance.entry_time}")

            # Sauvegarder les changements
            db.session.commit()
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
