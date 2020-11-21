import time
import json
from phue import Bridge
import paho.mqtt.client as mqtt

config = {}
with open("config.json", "r") as file:
    config = json.loads(file.read())

sensor_topic_id = config.get("sensor_topic_id")
indicator_light_id = config.get("indicator_light_id")
bridge_ip = config.get("bridge_ip")

b = Bridge(ip=bridge_ip, config_file_path="/data/.python_hue")
b.connect()

def set_indicator_light_state(on: bool) -> None:
    print(f"Light was on state {b.get_light(6, 'on')}")
    b.set_light(indicator_light_id, 'on', on)
    print(f"Light set to state {on}")


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(sensor_topic_id)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, message):
    payload_string = message.payload.decode("utf-8")
    print(payload_string)

    payload = json.loads(payload_string)
    is_door_open = not payload.get("contact")
    set_indicator_light_state(is_door_open)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt-mosquitto", 1883, 60)

client.loop_forever()