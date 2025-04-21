import paho.mqtt.client as mqtt
import time
import random

cliente = mqtt.Client(client_id="sensor_temperatura", protocol=mqtt.MQTTv311)
cliente.connect("localhost", 1883, 60)

print("🌡️ Sensor de Temperatura Iniciado...")

while True:
    temperatura = round(random.uniform(20.0, 30.0), 2)
    cliente.publish("iot/temperatura", f"{temperatura}°C")
    print(f"Temperatura enviada: {temperatura}°C")
    time.sleep(2)
