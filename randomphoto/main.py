import os
import time
import random
import datetime
import threading
from gphotospy import authorize
from gphotospy.media import *
from gphotospy.album import *
from post_to_webservice import send_post_event_request

NEW_PHOTO_INTERVAL_SECONDS = int(os.getenv("NEW_PHOTO_INTERVAL", 30))

photo_buffer = []

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

def get_revelant_data(media_item: dict) -> (str, str, str, str, str):
    base_url = media_item.get("baseUrl")
    product_url = media_item.get("productUrl")
    width = media_item.get("mediaMetadata").get("width")
    height = media_item.get("mediaMetadata").get("height")
    creation_time = media_item.get("mediaMetadata").get("creationTime")

    return base_url, product_url, width, height, creation_time
class FillPhotoBufferThread:

    def __init__(self):
        CLIENT_SECRET_FILE = "client_secret.json"
        self.service = authorize.init(CLIENT_SECRET_FILE)

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        print("Not implemented")
        exit(1)

class RandomPhoto(FillPhotoBufferThread):
        
    def run(self):
        media_manager = Media(self.service)

        while True:
            # do not let photo buffer grow to big, stop if we have a buffer that is big enough
            if len(photo_buffer) >= 20:
                sleep_seconds = NEW_PHOTO_INTERVAL_SECONDS * 10
                print(f"Reached {len(photo_buffer)} photos in buffer (>20), sleeping for {sleep_seconds} seconds")
                time.sleep(NEW_PHOTO_INTERVAL_SECONDS)
                continue

            try:
                media_list = list(media_manager.search(get_random_data_range()))
            except:
                continue
            
            media = random.choice(media_list)
            base_url, product_url, width, height, creation_time = get_revelant_data(media)

            photo_buffer.append({
                "public_url": f"{base_url}=w{width}-h{height}",
                "private_url": product_url,
                "creation_time": creation_time
            })

            time.sleep(5)

class SameDayAnotherYear(FillPhotoBufferThread):

    def run(self):    
        media_manager = Media(self.service)

        today = datetime.date.today()
        count = 0
        for year in range(2007, datetime.date.today().year):
            today_in_another_year_filter = date(year, today.month, today.day)

            try:
                media_list = list(media_manager.search(today_in_another_year_filter))
            except:
                continue
            
            count += len(media_list)
            for media in media_list:
                base_url, product_url, width, height, creation_time = get_revelant_data(media)


                if next((item for item in photo_buffer if item["private_url"] == product_url), None):
                    continue

                photo_buffer.append({
                    "public_url": f"{base_url}=w{width}-h{height}",
                    "private_url": product_url,
                    "creation_time": creation_time
                })
        
        sleep_seconds = NEW_PHOTO_INTERVAL_SECONDS * len(photo_buffer)
        print(f"Got all {count} photos of today in other years, sleeping for {sleep_seconds} seconds")
        time.sleep(sleep_seconds)


def main() -> None:
    while True:
        random.shuffle(photo_buffer)

        if len(photo_buffer) < 1:
            seconds = 5
            print(f"No buffer in value, wait {seconds} seconds before next check")
            time.sleep(seconds)
            continue
        
        item = photo_buffer.pop()
        public_url, private_url, creation_time = item.get("public_url"), item.get("private_url"), item.get("creation_time")
        event_payload = {
            "person": {
                "id": "JAKBLU",
                "name": "Jakob",
            },
            "publicUrl": public_url,
            "privateUrl": private_url,
            "creationTime": creation_time,
        }
        event_type = "RANDOM_GOOGLE_PHOTO"
        
        print(f"Send random gooogle photo event, {len(photo_buffer)} left in queue")
        # print(event_payload)
        result = send_post_event_request(event_type, event_payload)

        time.sleep(NEW_PHOTO_INTERVAL_SECONDS)

if __name__ == "__main__":
    mode = os.getenv("RANDOM_PHOTO_MODE")
    if mode == "SAME_DAY_ANOTHER_YEAR":
        fill_photo_buffer_thread = SameDayAnotherYear()
    else:
        fill_photo_buffer_thread = RandomPhoto()
    
    main()