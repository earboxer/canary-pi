'''File'''
import paho.mqtt.client as mqtt
import os
import time
import sys

BROKER = sys.argv[2]
PORT = 1883
QOS = 0

# Callback when a message is published
def on_publish(client, userdata, mid):
    print("MQTT data published")
# Callback when a connection has been established with the MQTT broker
def on_connect(client, userdata, rc, *extra_params):
    print('Connected with result code='+str(rc))
# Callback when client receives a PUBLISH message from the broker
def on_message(client, data, msg):
    if msg.topic == sys.argv[1]:
        print("Received message: Note = ", int(msg.payload))
        os.system('sonic_pi play ' + int(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect(BROKER, PORT, 60)
client.subscribe(sys.argv[1], qos=QOS)
client.loop_start()

try:
    while True:
        # add a duration or stop this at some point
	wavname = sys.argv[1] + '.wav'
        os.system('arecord --device=hw:1,0 --format S16_LE --rate 44100 -c1 test.wav')
	os.system('scp test.wav ' + sys.argv[2] + ':~/' + wavname)
        client.publish(sys.argv[1] + "/newfile", wavname)
        time.sleep(3)
except KeyboardInterrupt:
    print('Done')
    client.disconnect()
