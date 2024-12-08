from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, PortaobjetoViewSet, UsuarioCreateView,base64_imagen_upload_api_view,ImagenViewSet#,UsuarioViewSet,imagen_count


router = DefaultRouter()
#router.register(r'usuarios', UsuarioViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'portaobjetos', PortaobjetoViewSet)
router.register(r'imagenes', ImagenViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('', views.index),  # Añadimos una nueva URL para la vista index 
    path('usuarios/crear/', UsuarioCreateView.as_view(),name='usuario-create'),
   # path('imagen/count/', imagen_count, name='imagegen-count'),   
    path("base64_imagen_upload", base64_imagen_upload_api_view,name="base64_imagen_upload",
),
]
