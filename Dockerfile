FROM python:3.9

ADD app.py /

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 2000

CMD ["python", "app.py"]
