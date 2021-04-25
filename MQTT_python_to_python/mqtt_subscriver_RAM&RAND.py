import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message : ",  str(message.payload.decode("utf-8")))


# https://mqtt.eclipseprojects.io/
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker)


client.loop_start()
client.subscribe("RAM")
client.subscribe("RAND")
client.on_message = on_message
while True:
    time.sleep(30)

#client.loop_stop()