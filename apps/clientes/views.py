from django.shortcuts import render

from apps.clientes.models import Clientes


# Create your views here.

def clientes_list(request):

    data_context = Clientes.objects.filter(nombre='magmi')

    return render(request, 'clientes/archivoclientes.html', context={'data': data_context})