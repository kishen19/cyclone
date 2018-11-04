from django.shortcuts import render, HttpResponse
from .models import floodpoint
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def handle(request):
    try:
        locationx = request.POST.get('lati')
        locationy = request.POST.get('longi')
        floodpoint.objects.create(localx=locationx, localy=locationy)
        print('Received data successfully')
        return HttpResponse('ok')
    except:
        print('Did not receive data')
        return HttpResponse('errors')
