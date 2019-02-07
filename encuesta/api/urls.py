from django.urls import path


from .views import QuestionList, QuestionDetail, ChoiceList

# Se definen los recursos a los que se hara referencia en las URLs
urlpatterns = [
    path('questions/', QuestionList.as_view()),
    path('questions/<uuid:pk>/', QuestionDetail.as_view()),
    path('choices/', ChoiceList.as_view())
]
