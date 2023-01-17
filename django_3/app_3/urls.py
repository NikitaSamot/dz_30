from django.urls import path
from . import views

urlpatterns = [
    path('', views.dz_3),
    path('Логин/', views.dz_3_3),
]