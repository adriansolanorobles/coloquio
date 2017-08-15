#Urls de app landing
from django.conf.urls import url
from .views import asistentes_create
app_name = 'asistentes'
urlpatterns = [
    url(r'^new/$',asistentes_new, name="asistentes_new"),


]