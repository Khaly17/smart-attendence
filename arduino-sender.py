import paho.mqtt.client as mqtt

# Configuration du broker MQTT
mqtt_broker_url = "test.mosquitto.org"  # Utilise le broker Mosquitto public
mqtt_broker_port = 1883                 # Port standard pour MQTT
topic = "attendance/topic"              # Topic où publier les messages
badge_id = "12346"                      # Simuler un badge_id pour un utilisateur

# Callback lors de la connexion réussie au broker MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT Broker at {mqtt_broker_url}!")
        # Publier le message avec badge_id sur le topic
        client.publish(topic, badge_id)
        print(f"Message publié sur le topic {topic} avec badge_id: {badge_id}")
    else:
        print(f"Échec de la connexion, code retour {rc}")

# Callback lors de la publication réussie
def on_publish(client, userdata, mid):
    print(f"Message publié avec succès (Message ID: {mid})")

# Initialiser le client MQTT
client = mqtt.Client()

# Définir les callbacks
client.on_connect = on_connect
client.on_publish = on_publish

# Connexion au broker MQTT
client.connect(mqtt_broker_url, mqtt_broker_port, 60)

# Démarrer la boucle réseau pour gérer la communication avec le broker
client.loop_start()

# Attendre un moment pour s'assurer que le message est envoyé
import time
time.sleep(5)

# Arrêter la boucle et terminer
client.loop_stop()
print("Fin du script de publication MQTT.")
