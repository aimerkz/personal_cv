FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY ../requirements.txt /app

RUN apt-get update && pip install -r ./requirements.txt --no-cache-dir \
    && rm -rf /var/lib/apt/lists/*

COPY ./ /app

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
