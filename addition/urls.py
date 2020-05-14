from django.urls import path

from . import views

app_name = "addition"

urlpatterns = [
    path('', views.Index, name='index'),
    path('add/', views.Addition, name='add'),
]