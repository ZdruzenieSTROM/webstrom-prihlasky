FROM python:3.13 AS static-files-builder

RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pipenv sync --system

COPY . ./

ENV DJANGO_SETTINGS_MODULE=signup_portal.static_files_settings

RUN python manage.py collectstatic --no-input

FROM nginx:1.28

COPY --from=static-files-builder /static /usr/share/nginx/html
