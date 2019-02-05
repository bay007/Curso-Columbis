import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Question

# Create your views here.


class VotacionView_claquiernombre(View):
    def get(self, request):
        # Aqui se puede poner la logica de negocio
        # accesos a bases de datos
        # validacion de los mismos
        # escritura de bases de datos.
        # Etc, Etc , Etc
        return HttpResponse("<h1>Hola Mundo</h1>")

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class QuestionsView(View):

    def get(self, request, uuid=None):
        # Aqui se puede poner la logica de negocio
        # accesos a bases de datos
        # validacion de los mismos
        # escritura de bases de datos.
        # Etc, Etc , Etc
        if uuid is None:
            questions = Question.objects.all()
            respuesta = []
            for q in questions:
                respuesta.append({"uuid": str(
                    q.uuid), "question_text": q.question_text, "publish_date": str(q.publish_date)})
        else:
            r = Question.objects.get(uuid=uuid)
            respuesta = {"uuid": str(r.uuid), "question_text": r.question_text,
                         "publish_date": str(r.publish_date)}

        return HttpResponse(json.dumps(respuesta, ensure_ascii=False), content_type="application/json")

    def post(self, request, uuid=None):
        print(request.POST)
        return HttpResponse(f"Hola{uuid}")

    def put(self, request):
        pass

    def delete(self, request):
        pass
