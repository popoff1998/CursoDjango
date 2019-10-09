from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from .models import Articulo


class ArticuloAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}

    def get_changeform_initial_data(self, request):
        return {'autor': request.user}

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)

    def render_change_form(self, request, context, *args, **kwargs):
        if not request.user.is_superuser:
            context['adminform'].form.fields['autor'].queryset = User.objects.filter(id=request.user.id)
        return super().render_change_form(request, context, *args, **kwargs)

admin.site.register(Articulo, ArticuloAdmin)
