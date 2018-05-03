'''Primary code section'''
import paho.mqtt.client as mqtt
import os
import time

BROKER = "localhost"
PORT = 1883
QOS = 0

# Callback when client receives a PUBLISH message from the broker
def on_message(client, data, msg):
	if msg.topic == "pi1/newfile":
		print("Received message: File = ", msg.payload)
	elif msg.topic == "pi2/newfile":
		print("Received message: File = ", msg.payload)
	print("Converting from .wav to .mid: ")
	os.system("waon -i ~pi/" + str(msg.payload.decode()) + " -o next.mid")


client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.subscribe("pi1/newfile", qos=QOS)
client.subscribe("pi2/newfile", qos=QOS)
client.loop_start()

try:
	while True:
		time.sleep(3)
except KeyboardInterrupt:
	print('Done')
	client.disconnect()
