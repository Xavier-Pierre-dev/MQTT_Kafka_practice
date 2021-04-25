from pykafka import KafkaClient
from pykafka.exceptions import SocketDisconnectedError, LeaderNotAvailable
import time
from itertools import islice


client = KafkaClient()
topic = client.topics['RAM']
consumer = topic.get_simple_consumer()
print(consumer)


for message in consumer:
    print("Kafka consumer receive msg numero : ", message.offset, " with value : ", message.value.decode("utf-8", "ignore"))

try:
    consumer.consume()
except (SocketDisconnectedError) as e:
    consumer = topic.get_simple_consumer()
    # use either the above method or the following:
    consumer.stop()
    consumer.start()

