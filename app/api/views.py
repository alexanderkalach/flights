from django.shortcuts import render
from django.http import HttpResponse

from kafka import KafkaProducer


def index(request):
    producer = KafkaProducer(bootstrap_servers='kafka:9092', api_version=(0,10))
    
    producer.send('test', b'some_message_bytes')
    return HttpResponse("Hey")
