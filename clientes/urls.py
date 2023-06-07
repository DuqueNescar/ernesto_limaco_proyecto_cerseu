from django.urls import path
from . import views

urlpatterns = [
    path('clientes_archivo/', views.clientes_list, name='clientes_archivo'),
]