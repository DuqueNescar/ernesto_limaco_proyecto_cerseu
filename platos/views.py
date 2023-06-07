from django.shortcuts import render
from platos.models import Platos

# Create your views here.
def platos_list(request):

    p = Platos(nombre="papa", nacionalidad='peruano',edad=16,procedencia='peruano')
    p.save()
    p = Platos(nombre="juan", nacionalidad='peruano', edad=55, procedencia='chile')
    p.save()
    p = Platos(nombre="tobias", nacionalidad='peruano', edad=45, procedencia='japon')
    p.save()


    data_context = Platos.objects.filter(nacionalidad='peru', edad=40)

    return render(request, 'platos/archivoplatos.html', context={'data': data_context})