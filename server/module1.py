'''simply echo back into the other pi'''
import sys
import os

dest = 'pi1'
if(sys.argv[1] == 'pi1'):
	dest = 'pi2'

message = sys.argv[2]
os.system( "mosquitto_pub -h localhost -t " + dest + "/queue -r -m '" + message + "'")
