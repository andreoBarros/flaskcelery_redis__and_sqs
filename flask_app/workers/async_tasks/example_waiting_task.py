import time

from worker import celery_worker


@celery_worker.task(name="example_task", queue="celery")
def example_task(some_string: str = "default-value", waiting_for: int = 6):
    print(some_string)
    time.sleep(waiting_for)
    print(f"waited for {waiting_for} -- " + some_string)

