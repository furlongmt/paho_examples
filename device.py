import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, rc):
	new_time = time.clock()
	print("It took %s seconds to connect" % str(new_time - current_time))
	print("Successfully conncected")
	client.subscribe("furlong")

def on_message(client, userdata, msg):
	new_time = time.clock()
	print("It took %s seconds to receive a message" % str(new_time - current_time))
	string = "Message received: \n \t Topic: %s \n \t Message %s"
	print(string % (msg.topic, str(msg.payload)))

def on_publish(mosq, obj, mid):
	pass
	#new_time = time.clock()
	#print("It took %s seconds to publish a message" % str(new_time - current_time))

def on_disconnect(pahoClient, obj, rc):
    print "Disconnected"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_disconnect = on_disconnect

current_time = time.clock()

#client.connect("172.19.48.104", 3000, 60)     #virtualbox
#client.connect("130.127.133.51", 9090, 60)   #cloudlab
client.connect("169.55.155.236", 9999, 60)   #VCL

i = 0

client.loop_start()

while i < 100 :
	current_time = time.clock()
	client.publish("solar", "This is the string for Topic: matthew")
	i += 1

while 1:
	pass


'''client.disconnect()



client.connect("128.110.152.35", 3000, 60)

time.sleep(1)

i = 0

while i < 50:
	client.loop()
	current_time = time.clock()
	client.publish("matthew", "This is the string for Topic: matthew")
	i += 1

client.disconnect()'''
