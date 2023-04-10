FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install Flask==2.1.1

CMD ["python", "app.py"]

