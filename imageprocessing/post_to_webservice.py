
import requests

def send_request(predicted_class, person_image):
    payload = {
        "personId": predicted_class,
        "personImage": str(person_image, "utf-8")
    }
    response = requests.post("http://localhost:8000/api/detected_person", json=payload)
    
    return response.ok