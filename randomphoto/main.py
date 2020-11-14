import os
import time
import random
import datetime
from gphotospy import authorize
from gphotospy.media import *
from gphotospy.album import *
from post_to_webservice import send_post_event_request

NEW_PHOTO_INTERVAL_SECONDS = int(os.getenv("NEW_PHOTO_INTERVAL", 30))

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

def get_random_photo_url() -> (str, str):
    CLIENT_SECRET_FILE = "client_secret.json"
    service = authorize.init(CLIENT_SECRET_FILE)

    album_manager = Album(service)
    album_list = album_manager.list()
    media_manager = Media(service)

    while True:
        random_range = get_random_data_range()
        try:
            media_list = list(media_manager.search(random_range))
            break
        except TypeError:
            pass

    media = random.choice(media_list)
    base_url = media.get("baseUrl")
    product_url = media.get("productUrl")
    width = media.get("mediaMetadata").get("width")
    height = media.get("mediaMetadata").get("height")
    creationTime = media.get("mediaMetadata").get("creationTime")

    return f"{base_url}=w{width}-h{height}", product_url

def main() -> None:
    while True:
        public_url, private_url = get_random_photo_url()
        event_payload = {
            "person": {
                "id": "JAKBLU",
                "name": "Jakob",
            },
            "publicUrl": public_url,
            "privateUrl": private_url,
        }
        event_type = "RANDOM_GOOGLE_PHOTO"
        result = send_post_event_request(event_type, event_payload)

        time.sleep(NEW_PHOTO_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()