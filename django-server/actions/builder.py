from actions.models import Person


class PayloadBuilder:
    @staticmethod
    def build_detected_person_payload(person: Person, image: str) -> dict:
        payload = {
            "image": image
        }
        if person:
            payload.update({
                "person": {
                    "id": person.id,
                    "last_name": person.last_name,
                    "first_name": person.first_name,
                }
            })
        return payload 
