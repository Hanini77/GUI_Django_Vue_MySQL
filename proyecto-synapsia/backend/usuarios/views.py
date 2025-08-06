from django.http import JsonResponse
from .models import Usuario

def lista_usuarios(request):
    usuarios = list(Usuario.objects.values())
    return JsonResponse(usuarios, safe=False)
