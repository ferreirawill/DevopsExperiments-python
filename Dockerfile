FROM python:3.10.6-slim

WORKDIR /application
COPY requirements.txt /application
RUN pip install -r requirements.txt 
COPY . /application
EXPOSE 7001
CMD ["python3", "main.py"]