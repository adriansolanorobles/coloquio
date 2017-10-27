#Urls de app landing
from django.conf.urls import url
from .views import asistentes_new, asistentes_create, asistentes_invitacion
app_name = 'asistentes'
urlpatterns = [
    url(r'^new/$',asistentes_new, name="asistentes_new"),  
    url(r'^create/$',asistentes_create, name="asistentes_create"),
    url(r'^asistentes_invitacion/$',asistentes_invitacion, name="asistentes_invitacion"),
    
]

