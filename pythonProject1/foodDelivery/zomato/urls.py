from . import views
from django.urls import path, include

urlpatterns = [
    path('create_order/', views.create_order),
    path('create_person/', views.create_person),
    path('read_orders', views.read_orders),
    path('read_order', views.read_order),
    path('fetch_by_city', views.fetch_by_city),
    path('person_update', views.person_update),
    path('person_delete', views.person_delete),
]
