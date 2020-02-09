FROM python:3.5-slim

LABEL maintainer="michdcode@gmail.com"

USER root

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME ScrabbleHelp

CMD ["python", "app.py"]