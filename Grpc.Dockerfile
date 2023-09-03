FROM python:3.11

WORKDIR /grpc

COPY . /grpc

RUN pip install pip-tools
RUN make install

CMD ["python", "manage.py", "grpcserver"]