from django.urls import path
from .views import create_employee,getting_data,getall,update,delete,current_data,delete_data

urlpatterns=[
    path('create_employee/',create_employee),
    path('getting_data/',getting_data),
    path('getall/',getall),
    path('update/',update),
    path('delete/',delete),
    path('current_data/',current_data),
    path('delete_data/',delete_data)
]