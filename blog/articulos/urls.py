from django.urls import path

from . import views

urlpatterns = [
    path('detalle/<slug:slug>', views.DetailView.as_view(), name='detalle')
]
