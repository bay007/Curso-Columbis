from django.shortcuts import get_object_or_404, render

from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from votacion.models import Choice, Question

from .serializers import ChoiceSerializer, QuestionSerializer


class QuestionList(APIView):
    def get(self, request):
        questions = Question.objects.all()
        # Aqui va el argumento many=True por que se espera mas de un elemento
        data = QuestionSerializer(questions, many=True).data
        return Response(data)

    # Aqui se define post por que no requiere parametros de entrada (es decir el uuid de un elemento)
    def post(self, request):
        new_question_data = request.data
        new_question = QuestionSerializer(data=new_question_data)
        if new_question.is_valid():
            new_question.save()
            return Response(new_question.data, status=status.HTTP_201_CREATED)
        return Response(new_question.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
    def get(self, request, pk):
        question = get_object_or_404(Question, uuid=pk)
        # Aqui NO va el argumento many por que se espera un y solo un elemento
        data = QuestionSerializer(question).data
        return Response(data)

    # Aqui se define el put y en general aquellos métodos que requieran que se les pase el uuid de un elemento para operar
    def put(self, request, pk):
        question = Question.objects.get(uuid=pk)
        question_serialized = QuestionSerializer(question, data=request.data)
        if question_serialized.is_valid():
            question_serialized.save()
            return Response(question_serialized.data, status=status.HTTP_201_CREATED)
        return Response(question_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = Question.objects.get(uuid=pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""Comentar las clases de arriba ambas y descomentar las dos de abajo"""
# class QuestionList(generics.ListCreateAPIView):
# queryset = Question.objects.all()
# serializer_class = QuestionSerializer


# class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
# queryset = Question.objects.all()
# serializer_class = QuestionSerializer


class ChoiceList(APIView):
    def get(self, request):
        choices = Choice.objects.all()
        serialized_choices = ChoiceSerializer(choices, many=True).data
        return Response(serialized_choices)


class ChoiceDetail(APIView):
    pass
