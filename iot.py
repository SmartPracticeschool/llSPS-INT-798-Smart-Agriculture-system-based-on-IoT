import time
import sys
import ibmiotf.application 
import ibmiotf.device

organization = "v9c1fm" 
deviceType = "A2"
deviceId = "A2"
authMethod = "token"
authToken = "12345678" 

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)
        if cmd.data['command']=='motoron':
                print("MOTOR ON IS RECEIVED")
                          
        elif cmd.data['command']=='motoroff':
                print("MOTOR OFF IS RECEIVED")
                
        if cmd.command == "setInterval":
                
                if 'interval' not in cmd.data:
                        print("Error - command is missing required information: 'interval'")
                else:
                        interval = cmd.data['interval']
        elif cmd.command == "print":
                if 'message' not in cmd.data:
                        print("Error - command is missing required information: 'message'")
                else:
                        output=cmd.data['message']
                        print(output)

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:
              
        deviceCli.commandCallback = myCommandCallback
deviceCli.disconnect()
