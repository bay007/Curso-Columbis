from django.urls import path

from .views import VotacionView_claquiernombre, QuestionsView


urlpatterns = [
    path("", VotacionView_claquiernombre.as_view()),
    path("questions/", QuestionsView.as_view()),
    path("questions/<uuid:uuid>/", QuestionsView.as_view())
]
