from django.shortcuts import render,redirect
from django.http import Http404
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.template import Context
from django.template.loader import render_to_string, get_template
from .forms import AsistentesForm
from datetime import datetime
from .models import Asistentes
# Create your views here.

def asistentes_new(request):
	form = AsistentesForm(request.POST or None)
	return render(request,'asistentes/asistentes.html',{'form':form})

def asistentes_create(request):	 
	if request.method == 'POST':
		form = AsistentesForm(request.POST or None)
		if form.is_valid():
			asistentes = form.save()
			ctx = {}
			to = []
			ctx['nombre_completo'] = asistentes.nombre + ' ' + asistentes.apellido_paterno + ' ' + asistentes.apellido_materno
			ctx['folio'] = "CAP" + '-' + str(asistentes.id) + '-' + datetime.now().strftime('%d%m%y')
			to.append(asistentes.correo)

			from_email = 'notificaciones@habilidadesparaadolescentes.com'
			subject = 'IV Coloquio de Atención Plena, Confirmación de registro'
			bcc = ['seldor492@gmail.com','jorge_alfamar@hotmail.com']
			body = get_template('asistentes/asistentes_correo_registro.html').render(Context(ctx))
			msg = EmailMessage(subject=subject, body=body, to=to, 
			from_email=from_email,
			bcc = bcc
			)
			msg.content_subtype = 'html'
			msg.send()

	return render(request,'asistentes/exito.html')

def asistentes_invitacion(request):
	asistentes_objects = Asistentes.objects.filter(pk__in=(6,12,14,15,16))
	ctx = {}
	to = []
	for asistente in asistentes_objects:

		ctx['nombre_completo'] = asistente.nombre + ' ' + asistente.apellido_paterno + ' ' + asistente.apellido_materno
		to.append(asistente.correo)
		from_email = 'notificaciones@habilidadesparaadolescentes.com'
		subject = 'IV Coloquio "Atención Plena: Teoría y aplicaciones"'
		bcc = ['seldor492@gmail.com','jorge_alfamar@hotmail.com']
		body = get_template('asistentes/asistentes_correo_invitacion.html').render(Context(ctx))
		msg = EmailMessage(subject=subject, body=body, to=to, 
		from_email=from_email,
		bcc = bcc
		)
		#msg.attach_file('/home/ubuntu/proyecto_coloquio/coloquio/static/images/Cartel_IV_Coloquio_AP_reprogramado.jpg')
		#msg.attach('/images/Cartel_IV_Coloquio_AP_reprogramado.jpg', img_data, 'image/jpg')
		msg.content_subtype = 'html'
		msg.send()

	return render(request,'asistentes/exito.html', )



