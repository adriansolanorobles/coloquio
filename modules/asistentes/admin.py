from django.contrib import admin
from .models import Asistentes

class AsistentesAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'taller')
admin.site.register(Asistentes, AsistentesAdmin)