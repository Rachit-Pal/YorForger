FROM python:3.9.1-buster

WORKDIR /root/YorForger

COPY . .

RUN pip install -r requirements.txt

CMD ["python3","-m","YorForger"]
