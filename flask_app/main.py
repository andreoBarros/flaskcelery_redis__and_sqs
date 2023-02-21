from flask import Flask
from workers import worker_config
from core.config import settings
import os

app = Flask(__name__)


@app.route('/check_worker_config')
def check_worker_config():
    configuration = worker_config.setup(worker_type=settings.WORKER_TYPE)
    return str(configuration.get_config())


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
