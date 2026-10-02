# Create your views here.
from django.http import HttpResponse


def inicio(request):
    return HttpResponse("Servidor Django funcionando correctamente")
