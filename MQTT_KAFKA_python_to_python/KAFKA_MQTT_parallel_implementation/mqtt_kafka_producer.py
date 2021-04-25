import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import psutil
import time

# MQTT part :
mqtt_broker = "mqtt.eclipseprojects.io"
mqtt_client = mqtt.Client("MQTTProducer")
mqtt_client.connect(mqtt_broker)

# Kafka part :
kafka_client = KafkaClient(hosts='localhost:9092')
kafka_topic = kafka_client.topics["RAM"]
kafka_producer = kafka_topic.get_sync_producer()

while True:
    mem = psutil.virtual_memory()
    # print(mem)
    mqtt_client.publish("RAM", mem.percent)
    print("MQTT : just published : " + str(mem.percent) + " to topic RAM")

    kafka_producer.produce(str(mem.percent).encode("utf-8"))
    print("Kafka: Just published " + str(mem.percent) + " to topic RAM")
    time.sleep(3)

