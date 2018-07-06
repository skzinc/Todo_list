from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.details, name='detail'),
    path('add/', views.add, name="add"),
    path('delete/', views.delete, name="delete"),
]