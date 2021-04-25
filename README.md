# 🚀 MQTT & KAFKA : practice implementation 🚀

## stack :
* MQTT (paho-mqtt) => subscriver / publisher
* Kafka (pyKafka) => consumer / producer
* psutil 
* python

## Features :
* MQTT implementing on folder : `MQTT_python_to_python` 
* MQTT & Kafka working together on folder : `MQTT_KAFKA_python_to_python`
    * Kafka bridge on folder : `KAFKA_bridge`
    * Kafka & MQTT parallel implementation on folder : `KAFKA_MQTT_parallel_implementation`
    
## Quick started :
Follow the step explain inside the sub-project folder you want to run.

___
___
## Why this project :
I do this project to practice a little about MQTT whose are usefull for iOT communication. And Kafka like MQTT follow the publish/subscribe pattern for communication to topic but kafka is rather build for distributed event, streaming and storage and consumption of massive amount of data. So kafka can be use to complement mqtt. 

## what i learn and practice from this project :
With this project i learn about the concept of subscriver/publisher inside MQTT and Kafka to communicate inside topic. Concept of topic is near to the room concept for socket.io (websocket communication). 
I learn a little about psutil and i notice that my computer are not compatible with cpu method inside psutil that's one of the reason i use psutil.virtual_memory() to obtain ram usage for my usecase because the main goal of this project is to practice MQTT and Kafka.

## Some reflexion about this project 
With some research i find that's possible to use Kafka with Flask then create an interface for visualise data on a webpage so i guess it's also possible with django. That's something i can maybe try for display a chart using chart.js displaying ram usage data in percentage inside the brother when this data are coming from a kafka bridge.


# MQTT_Kafka_practice
