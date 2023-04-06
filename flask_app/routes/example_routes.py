from workers.async_tasks import example_tasks
from workers import worker_config
from core.config import settings
from flask import Blueprint

blueprint = Blueprint('urls', __name__)


@blueprint.route('/check_worker_config')
def check_worker_config():
    configuration = worker_config.setup(worker_type=settings.WORKER_TYPE)
    return str(configuration.get_config())


@blueprint.route('/divide_two_numbers/<first_number>/<second_number>')
def start_successful_task(first_number: int, second_number: int):
    example_tasks.divide_two_numbers.apply_async(
        kwargs={"first_number": first_number, "second_number": second_number}
    )

    return 'task_success'


@blueprint.route('/start_failure_task')
def start_failure_task():
    example_tasks.divide_two_numbers.apply_async(
        kwargs={"first_number": 5, "second_number": 0}
    )

    return 'task_failed_successfully'


@blueprint.route('/start_long_task/<seconds>')
def start_long_task(seconds: int):
    time = 60 if not seconds else int(seconds)
    example_tasks.wait_for_time.delay('waiting_for', time)
    return f'waiting for {time}'
