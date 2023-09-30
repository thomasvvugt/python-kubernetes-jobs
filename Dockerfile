FROM python:alpine

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt && rm -rf /requirements.txt

COPY app.py /app.py

CMD ["python", "/app.py"]
