#####################################
# primary.py contains the server code
# for CanaryPi.
#
# Authors: Zach DeCook and Jesse Kuntz
# Date: 05/07/18
#####################################

'''Primary code section'''
import paho.mqtt.client as mqtt
import os
import time
import sys
import commands


BROKER = "localhost"
PORT = 1883
QOS = 0

# Callback when client receives a PUBLISH message from the broker
def on_message(client, data, msg):
	name = msg.topic[:-len("/newfile")]
	print("Processing " +  msg.payload + " from " + name + "...")

	midifile = name + "next.mid"
	commands.getoutput("waon -i ~pi/" + str(msg.payload.decode()) + " -o " + midifile)

	command = "sh command.sh '" + midifile + "'"
	note = commands.getoutput( command )

	os.system( "python module.py '" + name + "' '" + note + "'" )

client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, PORT, 60)
print( "Subscribing to " )
for x in range(1,len(sys.argv)):
	print(sys.argv[x])
	client.subscribe(sys.argv[x] + "/newfile", qos=QOS)
client.loop_start()
print( "..." )

try:
	while True:
		time.sleep(3)
except KeyboardInterrupt:
	print('Done')
	client.disconnect()
