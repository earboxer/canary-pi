'''File'''
import paho.mqtt.client as mqtt
import os
import time

BROKER = "iot.cs.calvin.edu"
PORT = 1883
QOS = 0

# Callback when a connection has been established with the MQTT broker
def on_connect(client, userdata, rc, *extra_params):
 print('Connected with result code='+str(rc))
# Callback when client receives a PUBLISH message from the broker
def on_message(client, data, msg):
 if msg.topic == "pi1":
    print("Received message: Note = ", int(msg.payload))
    os.system('sonic_pi play ' + int(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.subscribe("pi1", qos=QOS)
client.loop_start()
