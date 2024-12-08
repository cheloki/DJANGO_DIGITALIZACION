from django.contrib import admin
from .models import Usuario, Portaobjeto, Imagen, Categoria, PortaobjetoCategoria

admin.site.register(Usuario)
admin.site.register(Portaobjeto)
admin.site.register(Imagen)
admin.site.register(Categoria)
admin.site.register(PortaobjetoCategoria)
