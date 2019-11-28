
import requests

def send_request(person_image, predicted_class):
    payload = {
        "person_id": predicted_class,
        "image": person_image
    }
    response = requests.post("http://localhost:8000/api/detected_person", json=payload)
    
    return response.ok