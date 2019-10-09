from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request):
        return HttpResponse('result')

    def post(self, request):
        # <view logic>
        return HttpResponse('result')


class DetailView(View):
    template_name = 'detail.html'

    def get(self, request, slug):
        return render(request, self.template_name, {'id': slug})
