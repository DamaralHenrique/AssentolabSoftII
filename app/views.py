from django.shortcuts import render
import requests
import json

# Create your views here.
def hello_world(request):
    estadio_id = 1 #request.GET['estadio_id']
    lugares = list(get_lugares(estadio_id))
    # print(lugares)
    return render(request, 'assentos.html', {'lugares':lugares})

def get_lugares(estadio_id):

    print("get_lugares")

    payload = {'estadio_id': estadio_id}
    resp = requests.get('http://172.17.0.2:8000/lugares', params=payload)

    # print(resp.status)
    resp = resp.json()

    print(resp)
    
    return resp