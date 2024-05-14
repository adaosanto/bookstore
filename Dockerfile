FROM ubuntu/postgres

RUN apt update && apt upgrade -y && \
    apt install curl -y && \
    apt install python3 -y && \
    apt-get install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt install python3.11 -y && \
    apt-get install -y --no-install-recommends netcat 

RUN curl -sS -O https://bootstrap.pypa.io/get-pip.py | python3.11
RUN python3.11 get-pip.py

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
ENV GNUPG_HOME $HOME/.gnupg
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
RUN mkdir $GNUPG_HOME 


WORKDIR $APP_HOME
COPY . $APP_HOME

RUN python3.11 -m pip install poetry
RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi
RUN chown -R app:app $HOME

RUN sed -i 's/\r$//g'  $APP_HOME/build/entrypoint.sh
RUN chmod +x  $APP_HOME/build/entrypoint.sh
RUN poetry run python3.11 manage.py genkey --gnupghome=$GNUPG_HOME

USER app

ENTRYPOINT ["/home/app/web/build/entrypoint.sh"]