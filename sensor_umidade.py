import paho.mqtt.client as mqtt
import time
import random

cliente = mqtt.Client(client_id="sensor_umidade", protocol=mqtt.MQTTv311)
cliente.connect("localhost", 1883, 60)

print("💧 Sensor de Umidade Iniciado...")

while True:
    umidade = round(random.uniform(40.0, 80.0), 2)
    cliente.publish("iot/umidade", f"{umidade}%")
    print(f"Umidade enviada: {umidade}%")
    time.sleep(2)
