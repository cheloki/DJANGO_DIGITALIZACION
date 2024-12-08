from django.core.exceptions import ValidationError



def validar_extension_imagen(value):
    if not value.name.endswith('.jpg'):
        raise ValidationError('El archivo debe ser una imagen con extensión .jpg.')
