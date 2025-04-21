import paho.mqtt.client as mqtt
import time
import random

cliente = mqtt.Client(client_id="sensor_pressao", protocol=mqtt.MQTTv311)
cliente.connect("localhost", 1883, 60)

print("🧭 Sensor de Pressão Iniciado...")

while True:
    pressao = round(random.uniform(990.0, 1025.0), 2)
    cliente.publish("iot/pressao", f"{pressao} hPa")
    print(f"Pressão enviada: {pressao} hPa")
    time.sleep(2)
