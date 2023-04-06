FROM python:3.12-rc-slim
ADD . .

#libssl3 required by pycurl from unstable debian (as of now)
RUN echo "deb http://deb.debian.org/debian unstable main" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y libssl3/unstable
RUN apt-get install -y libcurl4-openssl-dev/unstable libssl-dev/unstable curl python-dev


RUN pip install -r requirements.txt

WORKDIR /flask_app
CMD python app.py