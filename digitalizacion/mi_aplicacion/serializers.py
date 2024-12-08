from rest_framework import serializers

from drf_extra_fields.fields import Base64ImageField
from .models import Usuario, Categoria, Portaobjeto, Imagen

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class PortaobjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portaobjeto
        fields = '__all__'

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'


class ImagenBase64Serilizer(serializers.ModelSerializer):
    archivo = Base64ImageField(required=False)
    class Meta:
        model = Imagen
        fields = [ "descripcion","archivo","portaobjeto"]
