import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, rc):
	print("Successfully conncected")
	client.subscribe("solar")

def on_message(client, userdata, msg):
	string = "Message received: \n \t Topic: %s \n \t Message %s"
	print(string % (msg.topic, str(msg.payload)))

def on_publish(mosq, obj, mid):
	pass

def on_disconnect(pahoClient, obj, rc):
    print "Disconnected"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_disconnect = on_disconnect

#client.connect("172.19.48.104", 3000, 60)
#client.connect("128.110.152.35", 3000, 60)
client.connect("169.55.155.236", 9999, 60)   #VCL

client.loop_start()


'''i = 0

while i < 50:	
	client.loop()
	client.publish("furlong", "This is the string for Topic: furlong")
	i += 1

'''
while 1:
	pass
