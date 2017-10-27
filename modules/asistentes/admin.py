from django.contrib import admin
from .models import Asistentes

class AsistentesAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'apellido_paterno', 'apellido_materno', 'taller', 'correo')
admin.site.register(Asistentes, AsistentesAdmin)