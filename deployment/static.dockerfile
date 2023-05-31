FROM python:3.11 AS static-files-builder

RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pipenv sync --system

COPY . ./

ENV DJANGO_SETTINGS_MODULE=signup_portal.production
ENV DJANGO_SECRET_KEY=very-secret-key

RUN python manage.py collectstatic --no-input

FROM nginx:1.25

COPY --from=static-files-builder /static /usr/share/nginx/html
