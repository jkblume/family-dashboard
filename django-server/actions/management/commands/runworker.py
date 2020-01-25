from datetime import datetime
import logging
import time
import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from actions.builders import PayloadBuilder
from actions.models import StravaAthlete, AppPerson, StravaActivity
from eventstream.models import Event

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    @staticmethod
    def get_access_token(strava_athlete: StravaAthlete) -> str:
        if datetime.fromtimestamp(strava_athlete.expires_at) > datetime.now():
            return strava_athlete.access_token

        data = {
            "client_id": settings.STRAVA_CLIENT_ID,
            "client_secret": settings.STRAVA_CLIENT_SECRET,
            "grant_type": "refresh_token",
            "refresh_token": strava_athlete.refresh_token,
        }
        response = requests.post(url="https://www.strava.com/oauth/token", json=data)

        response_data = response.json()
        strava_athlete.refresh_token = response_data.get("refresh_token")
        strava_athlete.access_token = response_data.get("access_token")
        strava_athlete.expires_at = response_data.get("expires_at")
        strava_athlete.save()
        logger.info(f"Refreshed access token for athlete {strava_athlete.athlete_id}")
        return strava_athlete.access_token

    @staticmethod
    def poll_strava_activities():
        for strava_athlete in StravaAthlete.objects.all():
            access_token = Command.get_access_token(strava_athlete)

            last_strava_activity = (
                StravaActivity.objects.filter(strava_athlete=strava_athlete)
                .order_by("start_date")
                .last()
            )

            after = datetime(year=2020, month=1, day=1)
            if last_strava_activity is not None:
                after = last_strava_activity.start_date

            query_params = f"?after={after.timestamp()}"
            response = requests.get(
                url=f"https://www.strava.com/api/v3/athlete/activities{query_params}",
                headers={"Authorization": f"Bearer {access_token}"},
            )

            for activity in response.json():
                activity_id = str(activity.get("id"))
                if StravaActivity.objects.filter(activity_id=activity_id).exists():
                    continue

                app_person = AppPerson.objects.filter(
                    app=AppPerson.App.STRAVA, app_specific_id=strava_athlete.athlete_id
                ).first()

                person = None
                if app_person is not None:
                    person = app_person.person

                event_frontend_payload = PayloadBuilder.build_strava_activity_frontend_payload(
                    person
                )
                Event.objects.create(
                    event_type=Event.EventType.STRAVA_ACTIVITY,
                    frontend_payload=event_frontend_payload,
                )

                StravaActivity.objects.create(
                    strava_athlete=strava_athlete,
                    activity_id=activity_id,
                    start_date=activity.get("start_date"),
                )

            logger.info([item.get("id") for item in response.json()])

    def handle(self, *args, **options):
        StravaAthlete.objects.create(
            athlete_id=14096134,
            access_token="42fe61fd45543206ee521dbde74a1edeacaf0927",
            refresh_token="a0cb279ac95e95476b54e058d1a23d1be57fae2c",
            scope="activity:read",
            expires_at=1580004371,
        )

        StravaAthlete.objects.create(
            athlete_id=31294492,
            access_token="069213256782a84d3368ddba214a99c4a40d5e87",
            refresh_token="90f96d0bd464e0bfebea33371f81660a5806122e",
            scope="activity:read",
            expires_at=1580006506,
        )

        while True:
            Command.poll_strava_activities()
            time.sleep(10)
