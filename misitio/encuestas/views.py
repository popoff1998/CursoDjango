from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, Http404
from django.views import View
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Pregunta, Opcion


class IndexView(View):
    template_name = 'encuestas/index.html'

    def get(self, request):
        lista_ultimas_preguntas = Pregunta.objects.order_by('-creacion')[:5]
        context = {'lista_ultimas_preguntas': lista_ultimas_preguntas}
        return render(request, self.template_name, context)


class DetailView(View):
    template_name = 'encuestas/detail.html'

    def get(self, request, pregunta_id):
        # pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
        try:
            pregunta = Pregunta.objects.get(pk=pregunta_id)
        except Pregunta.DoesNotExist:
            raise Http404("La pregunta no existe")
        return render(request, self.template_name, {'pregunta': pregunta})


class ResultsView(View):
    template_name = 'encuestas/results.html'

    def get(self, request, pregunta_id):
        pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
        return render(request, 'encuestas/results.html', {'pregunta': pregunta})


class VoteView(View):

    def post(self, request, pregunta_id):
        pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
        try:
            opcion_seleccionada = pregunta.opcion_set.get(pk=request.POST['opcion'])
        except (KeyError, Opcion.DoesNotExist):
            return render(request, 'encuestas/detail.html', {'pregunta': pregunta, 'mensaje_error': "No has seleccionado una opción.", })
        else:
            opcion_seleccionada.votos += 1
            opcion_seleccionada.save()
        return HttpResponseRedirect(reverse('encuestas:results', args=(pregunta.id,)))
