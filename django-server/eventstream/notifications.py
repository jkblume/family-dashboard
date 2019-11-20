import json

from django_redis import get_redis_connection


class RedisNotificationService(object):
    @staticmethod
    def publish_notification(user_id: str, event: str, payload: dict):
        connection = get_redis_connection("default")
        connection.publish(
            f"notifications_gamification_{user_id}_{event}", json.dumps(payload)
        )


class ConsoleNotificationService(object):
    @staticmethod
    def publish_notification(user_id: str, event: str, payload: dict):
        print("NOTIFICATION", user_id, event, payload)
