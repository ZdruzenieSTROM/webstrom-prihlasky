FROM python:3.12

RUN pip install pipenv gunicorn

WORKDIR /app

COPY . ./

RUN pipenv sync --system

EXPOSE 80

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:80", "signup_portal.wsgi" ]
