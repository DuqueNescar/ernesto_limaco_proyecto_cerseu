from django.urls import path
from . import views

urlpatterns = [
    path('mesero_archivo/', views.mesero_list, name='mesero_archivo'),
]