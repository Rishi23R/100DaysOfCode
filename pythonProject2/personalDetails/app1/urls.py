from django.urls import path
from .import views
urlpatterns=[
    path('addDetails/',views.add_details),
    path('readDetails/',views.read_details)
]