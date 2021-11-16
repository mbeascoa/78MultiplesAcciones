from django.urls import path

from accionesboton import views

urlpatterns = [
    path('', views.index, name='index'),
    path('multiples', views.calcular, name='calcular'),

]