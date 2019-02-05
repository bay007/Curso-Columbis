from django.urls import path

from .views import VotacionView_claquiernombre


urlpatterns = [
    path("", VotacionView_claquiernombre.as_view())
]
