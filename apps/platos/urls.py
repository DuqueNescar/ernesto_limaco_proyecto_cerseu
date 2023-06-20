from django.urls import path
from . import views

urlpatterns = [
    path('platos_archivo/', views.platos_list, name='platos_archivo'),

    path("platos_list_vc", views.PlatosList.as_view(), name="platos_list_vc"),

    # URLs Serializers
    path('platos_list_serializer/', views.ListPlatosSerializer, name="owner_list_ssr"),




]

