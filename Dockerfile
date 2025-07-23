FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

# Change default port to 8003 to avoid "port is already allocated" error
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]
