
from django.urls import path

from rest_framework_swagger.views import get_swagger_view

from .views import ChoiceList, QuestionDetail, QuestionList

schema_view = get_swagger_view(title='API Votaciones')


# Se definen los recursos a los que se hara referencia en las URLs
urlpatterns = [
    path('docs/', schema_view),
    path('questions/', QuestionList.as_view()),
    path('questions/<uuid:pk>/', QuestionDetail.as_view()),
    path('choices/', ChoiceList.as_view())
]
