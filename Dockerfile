FROM python:3.7.10-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /flask_skeleton

RUN pip install --upgrade pip
COPY requirements.txt /flask_skeleton/
RUN pip install -r requirements.txt

COPY . /flask_skeleton/

CMD ["python", "./app.py"]