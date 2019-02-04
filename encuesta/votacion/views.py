from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
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
