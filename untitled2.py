import paho.mqtt.client

DATACAKE_TOKEN = "d5b753373788330b2243eb8091255d460d2eec92"

def on_connect(client, userdata, flags, rc):
    print('conectando (%s)' % client._client_id)
    client.subscribe(topic='dtck-pub/gateway-1/f0965f63-44ea-4b87-a2fc-469c45841823/LITORS_STRING', qos=2)
    
def on_message(client, userdata, msg):
    print(str(msg.payload))
    
    
    
    print('topico %s' % msg.topic)
    print('message %s' % msg.payload)
    print('qos %d" %s' % msg.qos)

def main():
    client = paho.mqtt.client.Client(client_id="python", clean_session=False)
    client.tls_set()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(DATACAKE_TOKEN, DATACAKE_TOKEN)
    client.connect("mqtt.datacake.co", 8883, 60)
    client.publish("dtck-pub/gateway-1/f0965f63-44ea-4b87-a2fc-469c45841823/LITROS",1)
    client.loop_forever()
    
if __name__ == '__main__' :
    main()