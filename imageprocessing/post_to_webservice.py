
import requests

def send_request():
    payload = {
        "person_id": "7b50b7f5-43a3-4ce7-b3c2-15cb554ce085"
    }
    response = requests.post("http://localhost:8000/api/detected_person", json=payload)
    
    return response.ok