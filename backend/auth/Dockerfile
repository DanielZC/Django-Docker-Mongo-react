FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
COPY requirements.txt /app/
RUN python -m pip install -r requirements.txt
COPY . /app/