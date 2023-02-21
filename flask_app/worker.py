from workers import worker_config
from celery import Celery
from core.config import settings


def worker_init() -> Celery:
    worker = Celery(__name__)
    configuration = worker_config.setup(worker_type=settings.WORKER_TYPE)
    worker.conf.update(configuration.get_config())
    return worker


celery_worker = worker_init()


def new_worker_instance():
    worker_config.import_tasks()
    celery_worker.autodiscover_tasks()
    celery_worker.worker_main(
        argv=[
            "worker",
            "-E",
            "--loglevel=info",
            # "--concurrency=1" Optional concurrency, for synchronous tasks
        ]
    )


if __name__ == "__main__":
    new_worker_instance()
