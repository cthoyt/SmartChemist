FROM python:3.11

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --requirement requirements.txt

COPY . /app
WORKDIR /app/smart_chemist_backend
RUN python manage.py migrate
RUN python add_patterns_to_db.py
