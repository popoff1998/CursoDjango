from django.urls import path
from . import views

app_name = 'encuestas'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pregunta_id>/', views.DetailView.as_view(), name='detail'),
    path('<int:pregunta_id>/resultados/', views.ResultsView.as_view(), name='results'),
    path('<int:pregunta_id>/votar/', views.VoteView.as_view(), name='vote'),
]
