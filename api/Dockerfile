FROM python:3.12.5-slim

WORKDIR /app

EXPOSE 8000

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "run.py"]