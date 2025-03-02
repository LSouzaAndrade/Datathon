FROM python:3.12.5-slim

WORKDIR /app

RUN apt-get update

RUN apt-get install -y awscli

EXPOSE 80

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "run.py"]