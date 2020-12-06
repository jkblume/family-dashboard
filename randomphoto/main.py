import os
import time
import random
import datetime
import requests
import threading
import base64
import logging
from datetime import timedelta
from gphotospy import authorize
from gphotospy.media import *
from gphotospy.album import *
from post_to_webservice import send_post_event_request

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

NEW_PHOTO_INTERVAL_SECONDS = int(os.getenv("NEW_PHOTO_INTERVAL", 30))

google_client_secret_json_as_base64 = os.getenv("GOOGLE_CLIENT_SECRET_JSON_AS_BASE64")
if not google_client_secret_json_as_base64:
    exit("Set GOOGLE_CLIENT_SECRET_JSON_AS_BASE64 env variable to start the module")

CLIENT_SECRET_PATH = "client_secret.json"

with open(CLIENT_SECRET_PATH, "w", encoding="utf-8") as file:
    encoded_google_client_secret_json_as_base64 = base64.b64decode(google_client_secret_json_as_base64)
    file.write(encoded_google_client_secret_json_as_base64.decode("utf-8"))

service = authorize.init(CLIENT_SECRET_PATH)
media_manager = Media(service)

def get_random_data_range() -> (date, date):
    start_date = datetime.date(2007, 1, 1)
    end_date = datetime.date.today()

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_start_date = start_date + datetime.timedelta(days=random_number_of_days)
    random_end_date = random_start_date + datetime.timedelta(5)

    random_start_date = date(year=random_start_date.year, month=random_start_date.month, day=random_start_date.day)
    random_end_date = date(year=random_end_date.year, month=random_end_date.month, day=random_end_date.day)

    return date_range(start_date=random_start_date, end_date=random_end_date)

def media_item_to_dict(media_item: dict, created_by_mode: str) -> dict:
    base_url = media_item.get("baseUrl")
    product_url = media_item.get("productUrl")
    width = media_item.get("mediaMetadata").get("width")
    height = media_item.get("mediaMetadata").get("height")
    creation_time = media_item.get("mediaMetadata").get("creationTime")

    return {
        "public_url": f"{base_url}=w{width}-h{height}",
        "private_url": product_url,
        "creation_time": creation_time,
        "link_creation_time": datetime.datetime.now(),
        "created_by_mode": created_by_mode
    }


def get_random_photo():
    media_list = []
    try:
        media_list = list(media_manager.search(get_random_data_range()))
    except Exception as e:
        print(f"Error on retrieving list: {e}")
    
    if len(media_list) == 0:
        print(f"List is empty (get_random_photo)")
        return None

    media = random.choice(media_list)
    photo_item = media_item_to_dict(media, "RANDOM_GOOGLE_PHOTO")

    return photo_item


def get_same_day_another_year_photo():    
    today = datetime.date.today()

    count = 0

    photos_of_the_day = []
    for year in range(2007, datetime.date.today().year):
        today_in_another_year_filter = date(year, today.month, today.day)

        try:
            media_list = list(media_manager.search(today_in_another_year_filter))
        except Exception as e:
            print(f"Error on retrieving list: {e}")
            continue
        
        photos_of_the_day += media_list
    
    if len(photos_of_the_day) == 0:
        print(f"List is empty (get_same_day_another_year_photo)")
        return None

    media = random.choice(photos_of_the_day)
    photo_item = media_item_to_dict(media, "SAME_DAY_ANOTHER_YEAR")

    return photo_item

def get_next_photo_item() -> dict:
    mode = os.getenv("RANDOM_PHOTO_MODE")
    if mode == "SAME_DAY_ANOTHER_YEAR":
        next_photo = get_same_day_another_year_photo()
    elif mode == "RANDOM_GOOGLE_PHOTO":
        next_photo = get_random_photo()
    else:
        next_photo = get_random_photo()

    # mainly if using same day another year mode or others that could lead to no photo for selected filter
    if next_photo is None:
        print(f"Did not found photo in first place - try it again with random photo")
        next_photo = get_random_photo()
    
    return next_photo

def main() -> None:
    while True:    
        current_hour = datetime.datetime.now().hour

        if 0 <= current_hour <= 6:
            print("Not generating new photos, its sleeping time")
            time.sleep(10)
            continue

        
        item = get_next_photo_item()

        if item is None:
            print("No photo found. Sleeping for 60 seconds and try it again...")
            time.sleep(60)
            continue
            

        event_payload = {
            "person": {
                "id": "JAKBLU",
                "name": "Jakob",
            },
            "publicUrl": item.get("public_url"),
            "privateUrl": item.get("private_url"),
            "creationTime": item.get("creation_time"),
            "mode": item.get("created_by_mode"),
        }
        event_type = "RANDOM_GOOGLE_PHOTO"
        
        print(event_payload)
        result = send_post_event_request(event_type, event_payload)

        time.sleep(NEW_PHOTO_INTERVAL_SECONDS)

main()