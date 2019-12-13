from actions.models import Person


class PayloadBuilder:
    @staticmethod
    def build_detected_person_payload(person: Person, image: str) -> dict:
        payload = {"data": {"image": image}, "activityType": "DETECTED_PERSON"}
        if person:
            payload.update(
                {
                    "person": {
                        "id": person.id,
                        "name": f"{person.first_name} {person.last_name}",
                    }
                }
            )
        return payload

    @staticmethod
    def build_strava_activity_payload(person: Person) -> dict:
        payload = {"activityType": "STRAVA_ACTIVITY"}
        if person:
            payload.update(
                {
                    "person": {
                        "id": person.id,
                        "name": f"{person.first_name} {person.last_name}",
                    }
                }
            )
        return payload
