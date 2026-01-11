# syntax=docker/dockerfile:1
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# створюємо non-root користувача
RUN useradd -m appuser

# В ідеалі - requirements.txt із зафіксованими версіями
COPY app /app
RUN pip install --no-cache-dir fastapi==0.110.0 uvicorn==0.29.0

USER appuser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
