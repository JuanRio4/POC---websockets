import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("📊 Dashboard conectado ao broker.")
    client.subscribe("iot/#")

def on_message(client, userdata, msg):
    print(f"[{msg.topic}] Mensagem recebida: {msg.payload.decode()}")

cliente = mqtt.Client(client_id="dashboard", protocol=mqtt.MQTTv311)
cliente.on_connect = on_connect
cliente.on_message = on_message
cliente.connect("localhost", 1883, 60)

cliente.loop_forever()
