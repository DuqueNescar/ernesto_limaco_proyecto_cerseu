from django.shortcuts import render
from meseros.models import Meseros


# Create your views here.
def mesero_list(request):

    p = Meseros(nombre="papa", precio=50,procedencia="peru")
    p.save()
    p = Meseros(nombre="camote", precio=50, procedencia="peru")
    p.save()
    p = Meseros(nombre="yuca", precio=50, procedencia="peru")
    p.save()


    data_context = Meseros.objects.filter(procedencia='peru', precio__gte=30)

    return render(request, 'meseros/archivomeseros.html', context={'data': data_context})