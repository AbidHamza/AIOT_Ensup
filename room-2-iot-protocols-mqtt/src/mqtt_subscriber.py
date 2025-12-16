#!/usr/bin/env python3
"""
Subscriber MQTT simple
Room 2 - AIoT Academy
"""

import json
import paho.mqtt.client as mqtt
from datetime import datetime


class MQTTSubscriber:
    """
    S'abonne à des topics MQTT et reçoit des messages
    """
    
    def __init__(
        self,
        broker_host: str = "localhost",
        broker_port: int = 1883,
        client_id: str = None
    ):
        """
        Initialise le subscriber MQTT
        
        Args:
            broker_host: Adresse du broker MQTT
            broker_port: Port du broker MQTT
            client_id: ID unique du client
        """
        self.broker_host = broker_host
        self.broker_port = broker_port
        
        # Créer le client MQTT
        self.client = mqtt.Client(client_id=client_id)
        
        # Callbacks
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.on_subscribe = self._on_subscribe
    
    def _on_connect(self, client, userdata, flags, rc):
        """Callback appelé lors de la connexion"""
        if rc == 0:
            print(f"✓ Connecté au broker MQTT ({self.broker_host}:{self.broker_port})\n")
        else:
            print(f"✗ Erreur de connexion, code: {rc}")
    
    def _on_subscribe(self, client, userdata, mid, granted_qos):
        """Callback appelé après l'abonnement"""
        print(f"✓ Abonné au topic (mid: {mid}, QoS: {granted_qos})\n")
    
    def _on_message(self, client, userdata, msg):
        """Callback appelé lors de la réception d'un message"""
        try:
            # Décoder le message
            payload = msg.payload.decode('utf-8')
            
            # Parser le JSON
            data = json.loads(payload)
            
            # Afficher les informations
            timestamp = datetime.now().strftime('%H:%M:%S')
            print(f"\n[{timestamp}] Message reçu:")
            print(f"  Topic: {msg.topic}")
            print(f"  QoS: {msg.qos}")
            print(f"  Données: {json.dumps(data, indent=4)}")
        
        except json.JSONDecodeError:
            print(f"\n[!] Message non-JSON reçu sur {msg.topic}: {msg.payload.decode('utf-8')}")
        except Exception as e:
            print(f"\n[!] Erreur lors du traitement du message: {e}")
    
    def subscribe(self, topic: str, qos: int = 1):
        """
        S'abonne à un topic
        
        Args:
            topic: Topic MQTT (peut contenir des wildcards + et #)
            qos: Quality of Service
        """
        self.client.subscribe(topic, qos)
        print(f"Abonnement demandé: {topic} (QoS: {qos})")
    
    def connect_and_listen(self):
        """Connecte le client et démarre l'écoute"""
        try:
            print(f"=== Subscriber MQTT - Room 2 ===\n")
            print(f"Connexion au broker {self.broker_host}:{self.broker_port}...")
            
            self.client.connect(self.broker_host, self.broker_port, 60)
            
            # Boucle d'écoute (bloquante)
            print("En attente de messages... (Ctrl+C pour arrêter)\n")
            self.client.loop_forever()
        
        except KeyboardInterrupt:
            print("\n\nArrêt du subscriber...")
            self.disconnect()
        except Exception as e:
            print(f"\n✗ Erreur: {e}")
            self.disconnect()
    
    def disconnect(self):
        """Déconnecte le client"""
        self.client.loop_stop()
        self.client.disconnect()
        print("✓ Déconnecté du broker MQTT")


def main():
    """Fonction principale"""
    # Créer le subscriber
    subscriber = MQTTSubscriber(
        broker_host="localhost",
        broker_port=1883,
        client_id="aiot-subscriber-001"
    )
    
    # S'abonner à tous les topics de température
    subscriber.subscribe("aiot-academy/+/temperature", qos=1)
    
    # Alternative: S'abonner à un device spécifique
    # subscriber.subscribe("aiot-academy/TEMP-001/#", qos=1)
    
    # Démarrer l'écoute
    subscriber.connect_and_listen()


if __name__ == "__main__":
    main()

