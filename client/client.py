#####################################
# client.py contains the client code
# for CanaryPi.
#
# Authors: Zach DeCook and Jesse Kuntz
# Date: 05/07/18
#####################################

'''File'''
import paho.mqtt.client as mqtt
import os
import time
import sys
import datetime
import commands

BROKER = sys.argv[2]
PORT = 1883
QOS = 0

# Callback when client receives a PUBLISH message from the broker
def on_message(client, data, msg):
    if msg.topic == sys.argv[1] + "/queue":
        print("Received message: " + str(int(msg.payload)) + ". Playing note...")
        if (int(msg.payload) > 40):
            os.system('sonic_pi play ' + str(int(msg.payload)) + ', sustain: 1.25')

client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.subscribe(sys.argv[1], qos=QOS)
client.subscribe(sys.argv[1] + "/queue", qos=QOS)
client.loop_start()

try:
    while True:
        # Modulo so it will overwrite old files
        wavname = str(int(time.time() * 10)%100) + sys.argv[1] + ".wav"
	sys.stdout.write( "Recording... " )
        commands.getoutput('arecord --device=hw:1,0 --format S16_LE --rate 48000 -c1 -d 1 test.wav')
	sys.stdout.write( "Copying file " + wavname + "... " )
        commands.getoutput('scp test.wav pi@' + sys.argv[2] + ':~/' + wavname)
	print( "Copied." )
        client.publish(sys.argv[1] + "/newfile", wavname)
	time.sleep(.1)
except KeyboardInterrupt:
    print('Done')
    client.disconnect()
