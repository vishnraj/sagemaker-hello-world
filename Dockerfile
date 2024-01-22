FROM python:3.7-slim

RUN pip install flask

COPY hello_world.py /opt/ml/hello_world.py

WORKDIR /opt/ml

EXPOSE 8080

ENTRYPOINT ["python3", "hello_world.py"]
