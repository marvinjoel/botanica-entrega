from django.urls import path
from plantas.views import PortadaView

urlpatterns = [
    path('', PortadaView.as_view()),
]