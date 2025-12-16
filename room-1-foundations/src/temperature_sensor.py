#!/usr/bin/env python3
"""
Simulateur de capteur de température
Room 1 - AIoT Academy
"""

import random
import time
from datetime import datetime
from dataclasses import dataclass
from typing import Dict


@dataclass
class TemperatureReading:
    """Représente une lecture de température"""
    sensor_id: str
    temperature: float  # en degrés Celsius
    timestamp: str
    unit: str = "celsius"


class TemperatureSensor:
    """
    Simule un capteur de température IoT
    
    Génère des valeurs de température réalistes autour d'une température de base
    avec une variation aléatoire (bruit) et une tendance saisonnière optionnelle.
    """
    
    def __init__(
        self, 
        sensor_id: str,
        base_temperature: float = 20.0,
        variation_range: float = 5.0,
        noise_level: float = 0.5
    ):
        """
        Initialise le capteur
        
        Args:
            sensor_id: Identifiant unique du capteur
            base_temperature: Température de base (défaut: 20°C)
            variation_range: Plage de variation (± variation_range)
            noise_level: Niveau de bruit (défaut: 0.5°C)
        """
        self.sensor_id = sensor_id
        self.base_temperature = base_temperature
        self.variation_range = variation_range
        self.noise_level = noise_level
        self.current_temperature = base_temperature
    
    def read(self) -> TemperatureReading:
        """
        Effectue une lecture de température
        
        Returns:
            TemperatureReading: Objet contenant la lecture
        """
        # Variation lente autour de la température de base
        variation = random.uniform(-self.variation_range, self.variation_range)
        
        # Bruit de mesure (variation rapide)
        noise = random.uniform(-self.noise_level, self.noise_level)
        
        # Calcul de la nouvelle température
        new_temperature = self.base_temperature + variation + noise
        
        # Lissage pour éviter les changements trop brutaux
        self.current_temperature = (
            0.7 * self.current_temperature + 0.3 * new_temperature
        )
        
        # Arrondir à 1 décimale
        temperature = round(self.current_temperature, 1)
        
        # Générer le timestamp
        timestamp = datetime.now().isoformat()
        
        return TemperatureReading(
            sensor_id=self.sensor_id,
            temperature=temperature,
            timestamp=timestamp
        )
    
    def to_dict(self) -> Dict:
        """
        Convertit la lecture en dictionnaire JSON
        
        Returns:
            Dict: Dictionnaire JSON-sérialisable
        """
        reading = self.read()
        return {
            "sensor_id": reading.sensor_id,
            "temperature": reading.temperature,
            "timestamp": reading.timestamp,
            "unit": reading.unit
        }


def main():
    """Fonction principale pour tester le simulateur"""
    print("=== Simulateur de capteur de température ===\n")
    
    # Créer un capteur
    sensor = TemperatureSensor(
        sensor_id="TEMP-001",
        base_temperature=22.0,
        variation_range=3.0,
        noise_level=0.3
    )
    
    # Simuler 10 lectures
    print("Simulation de 10 lectures de température:\n")
    for i in range(10):
        reading = sensor.read()
        print(f"[{i+1}] Capteur: {reading.sensor_id}")
        print(f"    Température: {reading.temperature}°C")
        print(f"    Timestamp: {reading.timestamp}\n")
        time.sleep(0.5)  # Attendre 0.5 seconde entre les lectures
    
    # Exemple de conversion JSON
    print("\n=== Exemple de format JSON ===")
    json_data = sensor.to_dict()
    import json
    print(json.dumps(json_data, indent=2))


if __name__ == "__main__":
    main()

