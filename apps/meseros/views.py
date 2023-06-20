from django.db.models import F, Q
from apps.meseros.models import Meseros
from django.http import HttpResponse
from apps.meseros.forms import MeserosForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.meseros.serializers import MeseroSerializer


# Create your views here.
def mesero_list(request):

     p = Meseros(nombre="papa", nacionalidad='peruano', edad=16, procedencia='peruano')
     p.save()
     p = Meseros(nombre="juan", nacionalidad='peruano', edad=55, procedencia='chile')
     p.save()
     p = Meseros(nombre="tobias", nacionalidad='peruano', edad=45, procedencia='japon')
     p.save()

     data_context = Meseros.objects.filter(procedencia='peru',edad__lt=30)

     return render(request, 'meseros/archivomeseros.html', context={'data': data_context})

def mesero_5(request):

    data_context = Meseros.objects.filter(procedencia='peru')
    Meseros.objects.update(edad=F('edad') + 10)

    return render(request, 'meseros/meseros5años.html', context={'data': data_context})

def mesero_search(request):

    query = request.GET.get('q', '')
    print("Query: {}".format(query))

    results = (
        Q(nombre__icontains=query)
    )

    data_context = Meseros.objects.filter(results)
    #data_context = Owner.objects.filter(results).distinct()


    return render(request, 'meseros/meseros_serch.html', context={'data':data_context, 'query':query})


def mesero_details(request):
    meseros = Meseros.objects.all()

    return render(request, 'meseros/meseros_details.html', context={'data': meseros})


def mesero_create(request):
    form = MeserosForm(request.POST)

    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        nacionalidad = form.cleaned_data['nacionalidad']
        edad = form.cleaned_data['edad']
        procedencia = form.cleaned_data['procedencia']

        form.save()
        return redirect('mesero_details')


    else:
        form = MeserosForm()

    return render(request, 'meseros/meseros_create.html', {'form': form})


def mesero_delete(request,id_meseros):

    print("ID Meseros_ {}".format(id_meseros))

    meseros = Meseros.objects.get(id=id_meseros)
    meseros.delete()

    return  redirect('mesero_details')

def mesero_edit(request,id_meseros):
    #print("ID Owner a editar  {}".format(id_owner))
    mesero =Meseros.objects.get(id=id_meseros)
    print("Datos del owner a editor: {}".format(mesero))
    form =MeserosForm(initial={'nombre':mesero.nombre, 'nacionalidad':mesero.nacionalidad,'edad':mesero.edad,'procedencia':mesero.procedencia})

    if request.method == 'POST':
        form = MeserosForm(request.POST, instance=mesero)
        if form.is_valid():
            form.save()
            return redirect('mesero_details')

    return render(request, 'meseros/meseros_update.html', context={'form':form})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def mesero_api_view(request):

    if request.method == 'GET':
        print("Ingresar a GET")
        queryset= Meseros.objects.all()
        serializers_class = MeseroSerializer(queryset,many=True)

        return Response(serializers_class.data,status=status.HTTP_200_OK)
        """seimorta status"""

    elif request.method =='POST':
        print("Data owner {}".format(request.data))
        serializers_class = MeseroSerializer(data=request.data)
        if serializers_class.is_valid():
            serializers_class.save()
            return Response(serializers_class.data, status=status.HTTP_201_CREATED)
        return Response(serializers_class.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def mesero_details_view(request, pk):
    mesero = Meseros.objects.filter(id=pk).first()


    if mesero:
        if request.method == 'GET':
            serializers_class = MeseroSerializer(mesero)
            return Response(serializers_class.data)


        elif request.method == 'PUT':
            serializers_class = MeseroSerializer(mesero, data=request.data)

            if serializers_class.is_valid():
                serializers_class.save()
                return Response(serializers_class.data)
            return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            mesero.delete()
            return Response('Owner ha sido eliminado correctamente de la BD', status=status.HTTP_200_OK)

