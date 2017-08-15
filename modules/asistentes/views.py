from django.shortcuts import render,redirect
from django.http import Http404
from .forms import AsistentesForm
from django.http import HttpResponse

# Create your views here.

def asistentes_new(request):
	form = AsistentesForm(request.POST or None)
	return render(request,'asistentes/asistentes.html',{'form':form})

def asistentes_create(request):	 
	 if request.method == 'POST':
	 	form = AsistentesForm(request.POST or None)
	 	if form.is_valid():
	 		asistentes = form.save()
	 return render(request,'asistentes/exito.html')