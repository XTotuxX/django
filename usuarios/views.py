import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


# Create your views here.
def lista_usuarios(request):
    usuarios = User.objects.all().order_by("username")
    return render(request, "lista_users.html", {"usuarios": usuarios})


@csrf_exempt
@require_POST
def crear_usuario(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error:", "No se pudo gestionar el JSON."})

    usuario = data.get("usuario", "").strip()
    email = data.get("email", "").strip()
    password = data.get("password", "").strip()

    errores = {}

    if not usuario:
        errores["usuario"] = "El usuario es obligatorio"
    if not email:
        errores["email"] = "El email es obligatorio"
    if not password or len(password) < 8:
        errores["password"] = (
            "El password es obligatorio y debe tener al menos 8 caracteres"
        )

    if errores:
        return JsonResponse(errores, status=400)

    return JsonResponse(
        {
            "mensaje": "Usuario creado correctamente",
            "usuario": usuario,
            "email": email,
            "password": password,
        },
        status=201,
    )
