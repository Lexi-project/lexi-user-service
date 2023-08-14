FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install pip-tools
RUN make install

CMD ["gunicorn", "user_service_project.wsgi:application", "--bind",  "0.0.0.0:8000"]