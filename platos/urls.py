from django.urls import path
from . import views

urlpatterns = [
    path('platos_archivo/', views.platos_list, name='platos_archivo'),
]