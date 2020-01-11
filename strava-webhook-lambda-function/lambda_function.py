import json
import logging
import requests
logger = logging.getLogger()
logger.setLevel(logging.INFO)

STRAVA_WEBHOOK_TOKEN = "ef981c9c-80d0-4ac4-aef9-755306d76b44"
REGISTERED_DASHBOARDS_URLS = [
    "http://familydashboard.ddnss.org:8000/strava/webhook",
    "http://jarlmax.ddnss.org:8000/strava/webhook",
]

def lambda_handler(event, context):
    # TODO implement
    if event.get('httpMethod') == 'GET':
        mode = event.get('queryStringParameters').get("hub.mode")
        token = event.get('queryStringParameters').get("hub.verify_token")
        challenge = event.get('queryStringParameters').get("hub.challenge")

        if mode != "subscribe" or token != STRAVA_WEBHOOK_TOKEN:
            return {'statusCode': 403}

        logger.info("Registered Webhook Handler")
        
        return {
            'statusCode': 200,
            'body': json.dumps({"hub.challenge": challenge})
        }
        
    if event.get('httpMethod') == 'POST':
        strava_webhook_event_data = json.loads(event.get('body'))
        
        logger.info(event)
        
        for url in REGISTERED_DASHBOARDS_URLS:
            try:
                requests.post(url=url, json=strava_webhook_event_data)
            except Exception as e:
                logger.info(f"Dashboard endpoint {url} not reachable with error: {e}")
        
        return {'statusCode': 200}
