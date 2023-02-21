FROM python:3.10-slim
ADD . /flask_app
WORKDIR /flask_app
RUN pip install -r requirements.txt
CMD python app.py