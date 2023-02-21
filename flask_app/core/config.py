from dataclasses import dataclass
from core.enum_models import CeleryWorkerType
import dotenv

# Reads from a .env in the main.py project folder
environment = dotenv.dotenv_values("flask_app/.env")


@dataclass
class FlaskAppSettings:
    WORKER_TYPE: CeleryWorkerType
    REDIS_BACKEND_URL: str
    REDIS_BROKER_URL: str

    SQS_REGION: str
    SQS_ACCESS_KEY: str
    SQS_SECRET_KEY: str
    SQS_BROKER_URL: str
    SQS_QUEUE_URL: str


settings = FlaskAppSettings(**environment)
