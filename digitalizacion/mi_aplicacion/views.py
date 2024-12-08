from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets, filters,generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Usuario, Categoria, Portaobjeto, Imagen
from .serializers import UsuarioSerializer, CategoriaSerializer, PortaobjetoSerializer,ImagenBase64Serilizer, ImagenSerializer
def index(request):
    return HttpResponse("Hola mundo")

#class UsuarioViewSet(viewsets.ModelViewSet):
#    queryset = Usuario.objects.all()
#    serializer_class = UsuarioSerializer
#    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#    filterset_fields = ['nombre', 'email']
#    search_fields = ['nombre', 'email']

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nombre']
    search_fields = ['nombre', 'descripcion']

class PortaobjetoViewSet(viewsets.ModelViewSet):
    queryset = Portaobjeto.objects.all()
    serializer_class = PortaobjetoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nombre', 'usuario__nombre', 'categorias__nombre']
    search_fields = ['nombre', 'descripcion', 'usuario__nombre', 'categorias__nombre']

class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [ 'portaobjeto__nombre']
    search_fields = ['descripcion', 'portaobjeto__nombre']

class UsuarioCreateView(generics.CreateAPIView,generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

#@api_view(['GET'])
#def imagen_count(request):
#    try:
#        cantidad = Imagen.objects.count()
#        return JsonResponse(
#            {"total_imagenes": cantidad},
#            safe = False,
#            status=200,
#        )
#    except Exception as e:
#        return JsonResponse(
#            {"error": str(e)},
#            safe = False,
#            status=500,
#        )

@api_view(["POST"])
def base64_imagen_upload_api_view(request):
    if request.method == "POST":
        data = request.data
        serializer = ImagenBase64Serilizer(data=data)
        if serializer.is_valid():
            archivo = serializer.save()
            data = serializer.data
            return Response(data=data)
        return Response(serializer.errors, status=400)