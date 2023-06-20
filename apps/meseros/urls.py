from django.urls import path
from . import views

urlpatterns = [
    path('mesero_archivo/', views.mesero_list, name='mesero_archivo'),
    path('mesero5_archivo/', views.mesero_5, name='mesero5_archivo'),
    path('mesero_serch/', views.mesero_search, name ='mesero_search'),

    path('mesero_create/', views.mesero_create, name='mesero_create'),
    path('mesero_details/', views.mesero_details, name ='mesero_details'),
    path('mesero_delete/<int:id_meseros>', views.mesero_delete, name ='mesero_delete'),
    path('mesero_edit/<int:id_meseros>', views.mesero_edit, name ='mesero_edit'),

# URLs DRF
    path('mesero_list_drf_def/', views.mesero_api_view, name='owner_list_drf_def'),
    path('mesero_detail_drf_def/<int:pk>', views.mesero_details_view, name='owner_detail_drf_def')




]