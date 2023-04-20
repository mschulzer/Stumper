from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Klub, Table

def floor(request):
    klubber = Klub.objects.all()
    borde = Table.objects.all()
    return render(request, "floor.html", { 'klubber': klubber, 'borde': borde })
