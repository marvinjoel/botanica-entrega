from django.shortcuts import render
from django.views.generic import TemplateView

from plantas.models import PlantasModels


class PortadaView(TemplateView):
    template_name = 'portada.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plantas'] = PlantasModels.objects.all()
        return context
