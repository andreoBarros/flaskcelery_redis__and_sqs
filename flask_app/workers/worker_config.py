from dataclasses import dataclass, asdict
from core.config import settings
from core.enum_models import CeleryWorkerType


@dataclass
class CeleryRedisConfig:
    result_backend: str
    broker_url: str

    def get_config(self) -> dict:
        return asdict(self)


@dataclass
class CelerySQSBrokerOptions:
    region: str
    predefined_queues: dict[str, dict[str, str]]


@dataclass
class CelerySQSConfig:
    broker_url: str
    broker_transport_options: CelerySQSBrokerOptions

    def get_config(self) -> dict:
        return asdict(self)


def setup(worker_type: CeleryWorkerType) -> CeleryRedisConfig | CelerySQSConfig:
    if worker_type.upper() == CeleryWorkerType.REDIS:
        return CeleryRedisConfig(
            result_backend=settings.REDIS_BACKEND_URL,
            broker_url=settings.REDIS_BROKER_URL

        )
    return CelerySQSConfig(
        broker_url=settings.SQS_BROKER_URL,
        broker_transport_options=CelerySQSBrokerOptions(
            region=settings.SQS_REGION,
            predefined_queues={
                "celery": {
                    "url": settings.SQS_QUEUE_URL,
                    "access_key_id": settings.SQS_ACCESS_KEY,
                    "secret_key_id": settings.SQS_SECRET_KEY
                }
            }
        ),
    )


def import_tasks():
    from workers.async_tasks import example_tasks
    _ = [example_tasks]
