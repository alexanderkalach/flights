from django.shortcuts import render
from django.http import HttpResponse

from kafka import KafkaProducer


def index(request):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    for _ in range(100):
        producer.send('test', b'some_message_bytes')
    return HttpResponse("Hey")
