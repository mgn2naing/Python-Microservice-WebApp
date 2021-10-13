FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN git clone https://github.com/mgn2naing/Python-Microservice-WebApp.git /app/
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000