FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd dos2unix

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/src/main

RUN dos2unix /app/infrastructure/docker/wait-for-db.sh && \
    chmod +x /app/infrastructure/docker/wait-for-db.sh

CMD ["/app/infrastructure/docker/wait-for-db.sh", "python", "app.py"]