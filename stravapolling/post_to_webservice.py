
import requests
import os

DJANGO_SERVER_HOST_API_URL = os.getenv("DJANGO_SERVER_HOST_API_URL", "http://localhost:8000")

def send_post_event_request(event_type: str, event_payload: dict) -> int:
    payload = {
        "eventType": event_type,
        "eventPayload": event_payload
    }
    try:
        response = requests.post(f"{DJANGO_SERVER_HOST_API_URL}/api/events/post_event/", json=payload)
    except:
        return 400
        
    return response.ok