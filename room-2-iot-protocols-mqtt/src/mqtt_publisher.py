#!/usr/bin/env python3
"""
Publisher MQTT simple
Room 2 - AIoT Academy
"""

import json
import time
import paho.mqtt.client as mqtt
from datetime import datetime
from temperature_sensor import TemperatureSensor  # Import depuis Room 1


class MQTTPublisher:
    """
    Publie des données de capteurs vers un broker MQTT
    """
    
    def __init__(
        self,
        broker_host: str = "localhost",
        broker_port: int = 1883,
        client_id: str = None
    ):
        """
        Initialise le publisher MQTT
        
        Args:
            broker_host: Adresse du broker MQTT
            broker_port: Port du broker MQTT
            client_id: ID unique du client (None = généré automatiquement)
        """
        self.broker_host = broker_host
        self.broker_port = broker_port
        
        # Créer le client MQTT
        self.client = mqtt.Client(client_id=client_id)
        
        # Callbacks
        self.client.on_connect = self._on_connect
        self.client.on_publish = self._on_publish
    
    def _on_connect(self, client, userdata, flags, rc):
        """Callback appelé lors de la connexion"""
        if rc == 0:
            print(f"✓ Connecté au broker MQTT ({self.broker_host}:{self.broker_port})")
        else:
            print(f"✗ Erreur de connexion, code: {rc}")
    
    def _on_publish(self, client, userdata, mid):
        """Callback appelé après la publication"""
        print(f"✓ Message publié (mid: {mid})")
    
    def connect(self):
        """Connecte le client au broker"""
        try:
            self.client.connect(self.broker_host, self.broker_port, 60)
            self.client.loop_start()
            time.sleep(0.5)  # Attendre la connexion
        except Exception as e:
            print(f"✗ Erreur de connexion: {e}")
            raise
    
    def publish_sensor_data(
        self,
        sensor: TemperatureSensor,
        topic: str = None,
        qos: int = 1,
        interval: float = 2.0
    ):
        """
        Publie les données d'un capteur périodiquement
        
        Args:
            sensor: Instance de capteur
            topic: Topic MQTT (défaut: aiot-academy/{sensor_id}/temperature)
            qos: Quality of Service (0, 1, ou 2)
            interval: Intervalle entre les publications (secondes)
        """
        if topic is None:
            topic = f"aiot-academy/{sensor.sensor_id}/temperature"
        
        print(f"\n=== Publication sur topic: {topic} ===")
        print(f"QoS: {qos}, Intervalle: {interval}s\n")
        
        try:
            while True:
                # Lire les données du capteur
                reading = sensor.read()
                
                # Convertir en JSON
                payload = json.dumps({
                    "sensor_id": reading.sensor_id,
                    "temperature": reading.temperature,
                    "timestamp": reading.timestamp,
                    "unit": reading.unit
                }, indent=2)
                
                # Publier
                result = self.client.publish(
                    topic=topic,
                    payload=payload,
                    qos=qos,
                    retain=False  # Ne pas retenir le message
                )
                
                if result.rc == mqtt.MQTT_ERR_SUCCESS:
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] "
                          f"Température: {reading.temperature}°C")
                else:
                    print(f"✗ Erreur de publication, code: {result.rc}")
                
                time.sleep(interval)
        
        except KeyboardInterrupt:
            print("\n\nArrêt du publisher...")
            self.disconnect()
    
    def disconnect(self):
        """Déconnecte le client"""
        self.client.loop_stop()
        self.client.disconnect()
        print("✓ Déconnecté du broker MQTT")


def main():
    """Fonction principale"""
    print("=== Publisher MQTT - Room 2 ===\n")
    
    # Créer un capteur de température
    sensor = TemperatureSensor(
        sensor_id="TEMP-001",
        base_temperature=22.0,
        variation_range=3.0
    )
    
    # Créer et connecter le publisher
    publisher = MQTTPublisher(
        broker_host="localhost",
        broker_port=1883,
        client_id="aiot-publisher-001"
    )
    
    try:
        publisher.connect()
        
        # Publier les données toutes les 2 secondes
        publisher.publish_sensor_data(
            sensor=sensor,
            topic="aiot-academy/TEMP-001/temperature",
            qos=1,
            interval=2.0
        )
    
    except KeyboardInterrupt:
        print("\nArrêt demandé par l'utilisateur")
    except Exception as e:
        print(f"\n✗ Erreur: {e}")
    finally:
        publisher.disconnect()


if __name__ == "__main__":
    main()

