#Dockerfile, image, container

FROM python:3.7.10-buster
ADD . /python-flask
WORKDIR /python-flask
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["gunicorn" , "-b", "0.0.0.0:8000", "app:app"]
