from django.urls import path

from . import views

urlpatterns = [
    path('detalle/<slug:slug>/', views.DetailView.as_view(), name='detalle'),
    path('autores/', views.AutoresView.as_view(), name='autores'),
    path('autor/<str:username>/', views.DetailAutorView.as_view(), name='autor'),
]
