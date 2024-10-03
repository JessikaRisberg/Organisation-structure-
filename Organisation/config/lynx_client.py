import paho.mqtt.client as mqtt
from lynx import Client

# Globala variabler
cli = None
mqttc = None

def create_lynx_client(api_key):
    cli = Client("https://lynx.iotopen.se", api_key)
    
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.tls_set()
    mqttc.username_pw_set(username="token-is-used", password=api_key)
    mqttc.connect("lynx.iotopen.se", 8883)
    
    return cli, mqttc
