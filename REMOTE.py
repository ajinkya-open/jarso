#REMOTE
import paho.mqtt.client as mqtt
import subprocess
USERNAME="ajinkya"
MQTTSERVER="geniewish.genieiot.com"
global direct_output


def getPubIp():
      direct_output = subprocess.check_output('curl ipinfo.io/ip', shell=True)
      return direct_output
    
def sendPubIp(pubIp):
      client.publish("att", payload=pubIp, qos=0, retain=False)
      
def on_connect(client, userdata, flags, rc):
    print("Connected ")
    client.subscribe("MyIp")
    client.publish("ID", payload=USERNAME, qos=0, retain=False)    
    print "got"

def on_message(client, userdata, msg):
    rec=str(msg.payload)
    r=rec.split()
    print r
    print r[0]
    print r[1]
    if(r[1]==USERNAME):
        print "meant for sapra"
        print "sending IP"
        dio=getPubIp()
        print dio
        sendPubIp(dio)
    print(msg.topic+" "+str(msg.payload))

while(True):
    try:
            client = mqtt.Client()
            client.on_connect = on_connect
            client.on_message = on_message
            client.connect(MQTTSERVER, 1883, 60)
            client.loop_forever()
    except Exception as e:
            print "ERROR : NO BROKER"+e.message
            



