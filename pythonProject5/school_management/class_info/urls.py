from django.urls import path
from . import views

urlpatterns = [
    path('class_info/', views.class_info, name='class_info'),
]