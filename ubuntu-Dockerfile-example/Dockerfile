FROM ubuntu:24.04

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

COPY . /app

RUN python3 -m pip install --no-cache-dir --break-system-packages -r requirements.txt

CMD ["python3", "app.py"]
