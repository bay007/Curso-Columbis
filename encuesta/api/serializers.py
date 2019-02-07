# Serializador,
# La serialización es el proceso de hacer una representación de los
# datos que podemos transferir a través de la red.
# La deserialización es su proceso inverso.

from rest_framework import serializers
from votacion.models import Choice, Question


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text', 'publish_date', )
