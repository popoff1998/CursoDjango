from django.shortcuts import render, reverse

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from rest_framework import generics

from .models import Articulo, Comentario
from .forms import ComentarioForm
from .serializers import ArticuloSerializer, ComentarioSerializer


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        articulos = Articulo.objects.all()
        return render(request, self.template_name, {'articulos': articulos})

    def post(self, request):
        # <view logic>
        return HttpResponse('result')


class DetailView(View):
    template_name = 'detail.html'

    def get(self, request, slug):
        articulo = Articulo.objects.get(slug=slug)
        form = ComentarioForm()
        context = {'articulo': articulo, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, slug):
        articulo = Articulo.objects.get(slug=slug)
        comentario = Comentario(articulo=articulo)
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid:
            form.save()
            form = ComentarioForm()
        return HttpResponseRedirect(reverse('detalle', args=(articulo.slug,)))


class AutoresView(View):
    template_name = 'autores.html'

    def get(self, request):
        autores = User.objects.filter(articulo__isnull=False)
        return render(request, self.template_name, {'autores': autores})


class DetailAutorView(View):
    template_name = 'detail_autor.html'

    def get(self, request, username):
        autor = User.objects.get(username=username)
        return render(request, self.template_name, {'autor': autor})


class ListaArticulosView(generics.ListCreateAPIView):
    model = Articulo
    serializer_class = ArticuloSerializer

    def get_queryset(self):
        queryset = Articulo.objects.all()
        id = self.request.query_params.get('id')
        slug = self.request.query_params.get('slug')
        if id:
            queryset = queryset.filter(id=id)
        elif slug:
            queryset = queryset.filter(slug__icontains=slug)
        return queryset


class ListaComentariosView(generics.ListCreateAPIView):
    model = Comentario
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        queryset = Comentario.objects.all()
        autor = self.request.query_params.get('autor')
        cuerpo = self.request.query_params.get('cuerpo')
        if autor:
            queryset = queryset.filter(autor__icontains=autor)
        elif cuerpo:
            queryset = queryset.filter(cuerpo__icontains=cuerpo)
        return queryset
