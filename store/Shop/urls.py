from django.urls import path
from . import views



urlpatterns= [
    path('', views.Shop, name='Shop'),
]
