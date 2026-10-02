# Create your views here.

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Producto


def lista_productos(request):
    return render(request, "lista.html")


def crea_producto(request):
    return render(request, "crear.html")


def listar_productos(request):
    productos = Producto.objects.all().order_by("id")
    data = []
    for p in productos:
        data.append(
            {
                "id": p.id,
                "nombre": p.nombre,
                "precio": str(p.precio),
                "descripcion": p.descripcion or "",
                "imagen_url": p.imagen.url if p.imagen else "",
            }
        )
    return JsonResponse(data, safe=False)


@csrf_exempt
def crear_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        descripcion = request.POST.get("descripcion")
        imagen = request.FILES.get("imagen")

        producto = Producto.objects.create(
            nombre=nombre, precio=precio, descripcion=descripcion, imagen=imagen
        )

        return JsonResponse(
            {"mensaje": "Producto creado con éxito", "id": producto.id}, status=201
        )
    return JsonResponse({"error": "Método no permitido"}, status=405)
