from django.contrib import admin
from .models import Asistentes

class AsistentesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Asistentes, AsistentesAdmin)from django.contrib import admin

# Register your models here.
