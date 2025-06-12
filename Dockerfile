# Dockerfile.dev
FROM python:3.10-slim

WORKDIR /app

# install dependencies early to leverage cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY . /app

EXPOSE 3003

# runtime: just start the Flask app
CMD ["sh", "-c", "alembic upgrade head && python run.py"]
