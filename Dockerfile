FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Enable pytest to find src
ENV PYTHONPATH=/app/src

CMD ["pytest", "-vv"]
