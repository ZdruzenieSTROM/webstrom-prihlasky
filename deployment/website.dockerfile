FROM python:3.11

WORKDIR /app

RUN pip install pipenv daphne

COPY . ./

RUN pipenv sync --system

ENV DJANGO_SETTINGS_MODULE=signup_portal.production
ENV PGSERVICEFILE /app/.pg_service.conf

EXPOSE 80

ENTRYPOINT [ "daphne", "-b", "0.0.0.0", "-p", "80", "signup_portal.asgi:application" ]
