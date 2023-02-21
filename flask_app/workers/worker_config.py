from dataclasses import dataclass, asdict
from core.config import environment
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
    if worker_type == CeleryWorkerType.REDIS:
        return CeleryRedisConfig(
            result_backend=environment.get("REDIS_BACKEND_URL"),
            broker_url=environment.get("REDIS_BROKER_URL")

        )
    return CelerySQSConfig(
        broker_url=environment.get("SQS_BROKER_URL"),
        broker_transport_options=CelerySQSBrokerOptions(
            region=environment.get("SQS_REGION"),
            predefined_queues={
                "celery": {
                    "url": environment.get("SQS_QUEUE_URL"),
                    "access_key_id": environment.get("SQS_ACCESS_KEY"),
                    "secret_key_id": environment.get("SQS_SECRET_KEY")
                }
            }
        ),
    )


def import_tasks():
    from workers.async_tasks import example_waiting_task
    _ = [example_waiting_task]


