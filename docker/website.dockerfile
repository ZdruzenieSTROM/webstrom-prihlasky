FROM python:3.13

RUN pip install pipenv daphne

WORKDIR /app

COPY . ./

RUN pipenv sync --system

ENV DJANGO_SETTINGS_MODULE=signup_portal.production_settings

CMD [ "daphne", "-b", "0.0.0.0", "-p", "80", "signup_portal.asgi:application" ]
