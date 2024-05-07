###########
# BUILDER #
###########

# pull official base image
FROM python:3.11.4-slim-buster as builder

# set work directory
WORKDIR /app

# set environment variables
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY . /app/


# pull official base image
FROM python:3.11.4-slim-buster

# create directory for the app user
RUN mkdir -p /home/app


# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles


WORKDIR $APP_HOME
COPY . $APP_HOME

RUN apt-get update && apt-get install -y --no-install-recommends netcat
RUN pip install poetry
RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi
RUN chown -R app:app $HOME

RUN sed -i 's/\r$//g'  $APP_HOME/build/entrypoint.sh
RUN chmod +x  $APP_HOME/build/entrypoint.sh


# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/home/app/web/build/entrypoint.sh"]