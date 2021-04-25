import paho.mqtt.client as mqtt
import time
from random import randrange, uniform

# https://mqtt.eclipseprojects.io/
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Random")
client.connect(mqttBroker)

while True:
    random = randrange(10)
    # print(mem)
    client.publish("RAND", random)
    print("just published : " + str(random) + " to topic RAND")
    time.sleep(3)