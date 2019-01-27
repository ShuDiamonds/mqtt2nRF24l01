import paho.mqtt.client as mqtt
import json
import serial

with open('/home/pi/Desktop/mqtt/mqtt_token.json') as f:
    jsn = json.load(f)
TOKEN = jsn["token"]
HOSTNAME = "mqtt.beebotte.com"
PORT = 8883
TOPIC = "ifttt_raspi/action"
CACERT = "mqtt.beebotte.com.pem"

def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    tmp = json.loads(str(msg.payload.decode("utf-8")))
    #print(tmp["data"])
    
    ctldataoff=[ord("A"),ord("0")]
    ctldataon=[ord("A"),ord("1")]
    if tmp["data"] == " on":
        print("LED on")
        with serial.Serial('/dev/ttyUSB0',9600,timeout=1) as ser:
            ser.write(ctldataon)
        ser.close()
    if tmp["data"] == " off":
        print("LED off")
        with serial.Serial('/dev/ttyUSB0',9600,timeout=1) as ser:
            ser.write(ctldataoff)
        ser.close()
def main():
    client = mqtt.Client()
    client.username_pw_set("token:%s"%TOKEN)
    client.on_connect = on_connect
    client.on_message = on_message
    client.tls_set(CACERT)
    client.connect(HOSTNAME, port=PORT, keepalive=60)
    client.loop_forever()

if __name__=='__main__': 
    main()