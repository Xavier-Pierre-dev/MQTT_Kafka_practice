import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received MQTT message : ",  str(message.payload.decode("utf-8")))


# https://mqtt.eclipseprojects.io/
mqtt_broker = "mqtt.eclipseprojects.io"
mqtt_client = mqtt.Client("MQTTConsumer")
mqtt_client.connect(mqtt_broker)


mqtt_client.loop_start()
mqtt_client.subscribe("RAM")
mqtt_client.on_message = on_message
while True:
    time.sleep(30)