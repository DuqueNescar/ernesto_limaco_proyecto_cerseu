from django.shortcuts import render
from apps.platos.models import Platos
from django.http import HttpResponse
from django.core import serializers as ssr
from django.views.generic import ListView


# Create your views here.
def platos_list(request):


    # p = Platos(nombre="papa", precio=50, procedencia="peru")
    # p.save()
    # p = Platos(nombre="camote", precio=50, procedencia="peru")
    # p.save()
    # p = Platos(nombre="yuca", precio=50, procedencia="peru")
    # p.save()


    data_context = Platos.objects.filter(procedencia='peru', precio__gt=40)

    return render(request, 'platos/archivoplatos.html', context={'data': data_context})


class PlatosList(ListView):
    model = Platos
    template_name = 'platos/platos_list_vc.html'


""" Seria Lazer """

def ListPlatosSerializer(request):
    lista_owner = ssr.serialize('json', Platos.objects.filter(precio__gte=50), fields=['nombre', 'precio', 'procedencia'])

    return HttpResponse(lista_owner, content_type="application/json")