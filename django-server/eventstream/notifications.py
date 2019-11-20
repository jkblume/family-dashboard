import json

from django_redis import get_redis_connection


class RedisNotificationService(object):
    @staticmethod
    def publish_notification(payload: dict):
        connection = get_redis_connection("default")
        connection.publish(f"notifications_server", json.dumps(payload))


class ConsoleNotificationService(object):
    @staticmethod
    def publish_notification(payload: dict):
        print("NOTIFICATION", payload)
