FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

CMD ["sh", "-c", "python manage.py makemigrations & python manage.py migrate"]
