from datetime import datetime
import logging
import time
import requests
import json
import os
from post_to_webservice import send_post_event_request


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

SERVER_STARTTIME = datetime.utcnow()

POLLING_INTERVAL = int(os.getenv("POLL_INTERVAL", 5))
STRAVA_CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
STRAVA_CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")

STRAVA_ATHLETES = []
with open("athletes.json", "r") as file:
    STRAVA_ATHLETES = json.loads(file.read())

def get_access_token(strava_athlete: dict) -> str:
    expires_at = datetime.fromtimestamp(strava_athlete.get("expires_at"))
    datetime_utcnow = datetime.utcnow()
    if expires_at > datetime_utcnow:
        logger.info(f"Access token still valid: access token expires at {expires_at.isoformat()}, current utc datetime {datetime_utcnow.isoformat()}")
        return strava_athlete.get("access_token")

    logger.info(f"Access token expired at {expires_at.isoformat()}, current utc datetime {datetime_utcnow.isoformat()}. Getting new token.")
    data = {
        "client_id": STRAVA_CLIENT_ID,
        "client_secret": STRAVA_CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": strava_athlete.get("refresh_token"),
    }
    response = requests.post(url="https://www.strava.com/oauth/token", json=data)

    response_data = response.json()
    strava_athlete["refresh_token"] = response_data.get("refresh_token")
    strava_athlete["access_token"] = response_data.get("access_token")
    strava_athlete["expires_at"] = response_data.get("expires_at")
    logger.info(f"Refreshed access token for athlete {strava_athlete.get('athlete_id')}")
    
    with open("athletes.json", "w") as file:
        file.write(json.dumps(STRAVA_ATHLETES))

    return strava_athlete.get("access_token")

def poll_strava_activities():
    for strava_athlete in STRAVA_ATHLETES:
        logger.info(f"Check strava athlete: {strava_athlete.get('athlete_id')}")
        access_token = get_access_token(strava_athlete)

        activities = strava_athlete.get("activities")
        last_strava_activity = activities[-1] if len(activities) > 0 else None

        after = SERVER_STARTTIME
        if last_strava_activity is not None:
            parseable_datetime_string = last_strava_activity.get("start_date").replace("Z", "+00:00")
            after = datetime.fromisoformat(parseable_datetime_string)

        logger.info(f"Getting activities since {after.isoformat()}")
        query_params = f"?after={after.timestamp()}"
        try:
            response = requests.get(
                url=f"https://www.strava.com/api/v3/athlete/activities{query_params}",
                headers={"Authorization": f"Bearer {access_token}"},
            )
        except Exception as e:
            logger.info(f"Error on getting activities: {e}")
            continue

        logger.info(response.json())

        for activity in response.json():
            activity_id = activity.get("id")
            if any(item['id'] == activity_id for item in activities):
                logger.info(f"Skip activity {activity_id} because we already processed it")
                continue

            activities.append({"id": activity.get("id"), "start_date": activity.get("start_date")})

            with open("athletes.json", "w") as file:
                file.write(json.dumps(STRAVA_ATHLETES))
            
            payload = {
                "person": {
                    "id": strava_athlete.get("person_id"),
                    "name": strava_athlete.get("person_name"),
                }
            }
            event_type = "STRAVA_ACTIVITY"

            logger.info(payload)
            result = send_post_event_request(event_type, payload)
            

def main() -> None:
    while True:
        poll_strava_activities()
        time.sleep(POLLING_INTERVAL)

if __name__ == "__main__":
    logger.info("Lets go...")
    main()