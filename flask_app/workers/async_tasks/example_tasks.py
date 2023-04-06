import time
from core.worker_exceptions import UnacceptableException
from celery import Task
from worker import celery_worker
from random import randint

RETRY_IN_SECONDS = 3


@celery_worker.task(
    name="wait_for_time",
    queue="celery",
    autoretry_for=(UnacceptableException,),
    retry_backoff=True,
    retry_backoff_max=20,
    retry_jitter=False,
)
def wait_for_time(some_string: str = "default-value", waiting_for: int = 6):
    print(some_string)

    random_number = randint(0, 10)
    print(random_number)

    time.sleep(int(waiting_for / 2))

    if not random_number % 2 == 0:
        raise UnacceptableException(code=413, info="A wild exception appears")
    print(f"waited for {waiting_for}/2")


@celery_worker.task(
    bind=True,
    name="divide_two_number",
    queue="celery",
    default_retry_delay=RETRY_IN_SECONDS,
    max_retries=3
)
def divide_two_numbers(self: Task, first_number: int = 6, second_number: int = 6):
    divide = first_number / second_number

    try:
        if first_number == 616:
            raise UnacceptableException(code=616, info="The Roman Empire, cannot be divided")
    except UnacceptableException as error:
        print("The Roman Empire, cannot be divided")

        if self.request.retries >= self.max_retries:
            print("The Roman Empire is eternal")
        else:
            self.retry(exc=error)

    print(f"{first_number}/{second_number} = {divide}")
