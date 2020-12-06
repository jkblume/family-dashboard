import time
import json
import logging
import requests
import paho.mqtt.client as mqtt

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

bridge_ip = "192.168.178.20"

with open("/data/.python_hue", "r") as file:
    data = json.loads(file.read())

username = data.get(bridge_ip).get("username")

front_floor_movement_sensor_topic = "zigbee2mqtt/0x842e14fffe05faaa"
child_bath_contact_sensor_topic = "zigbee2mqtt/0x00158d00045cdccc"
parent_time_toggle_button_topic = "zigbee2mqtt/0x842e14fffeff22b2"

indicator_light_id = 16
bedroom_light_id = 13

parent_time_button_state = False

def set_light_state(light_id: int, data: dict):
    response = requests.put(f"http://{bridge_ip}/api/{username}/lights/{light_id}/state", json=data)
    logger.info(response.json())


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    logger.info(f"Connected with result code {rc}")

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(front_floor_movement_sensor_topic)
    client.subscribe(child_bath_contact_sensor_topic)
    client.subscribe(parent_time_toggle_button_topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, message):
    global parent_time_button_state

    payload_string = message.payload.decode("utf-8")    
    logger.info(payload_string)
    payload = json.loads(payload_string)
    if message.topic == child_bath_contact_sensor_topic:
        is_door_open = not payload.get("contact")
        set_light_state(indicator_light_id, {"on": is_door_open})
    
    if message.topic == parent_time_toggle_button_topic:
        action = payload.get("action")
        if action is None:
            return

        set_light_state(bedroom_light_id, {"on": True})
        time.sleep(0.5)
        set_light_state(bedroom_light_id, {"on": False})
        parent_time_button_state = action == "on"
        logger.info(f"Parent time is {action}")

    if message.topic == front_floor_movement_sensor_topic:
        if not parent_time_button_state:
            logger.info("Some movement on the Front Floor, but no parent time...")
            return

        child_movement = payload.get("occupancy")
        if child_movement:
            set_light_state(bedroom_light_id, {"on": True, "xy": [0.7, 0.3]})
        if not child_movement:
            set_light_state(bedroom_light_id, {"on": False})

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt-mosquitto", 1883, 60)

client.loop_forever()