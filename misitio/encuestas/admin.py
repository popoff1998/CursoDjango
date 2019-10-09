from django.contrib import admin

# Register your models here.
from .models import Pregunta, Opcion


class OpcionInline(admin.StackedInline):
    model = Opcion
    extra = 0


class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('texto_pregunta', 'creacion')
    list_filter = ['creacion']
    fields = ['creacion', 'texto_pregunta']
    inlines = [OpcionInline]

admin.site.register(Pregunta, PreguntaAdmin )
admin.site.register(Opcion)
