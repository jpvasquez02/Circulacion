from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json
from django.views.generic.list import ListView
from circulacion.models import *
from circulacion.forms import *

@login_required
def home(request):
	template="index.html"
	return render_to_response(template)

def mapas(request):
	template="maps.html"
	return render_to_response(template)

def login(request):
	template='login.html'
	return render_to_response(template)

@login_required
def set_planes(request):
	#obtener informacion de los campos
	template='plan.html'
	if request.method=='POST':
		cp= request.POST.get("CodigoPlan","")
		cp2=request.POST.get("Nombre","")
		form=planesForm(request.POST)

		if form.is_valid():
			#Obtengo el modelo planes en la variable plan
			plan = planes()
			#Obtengo los Valores de Codigo y Nombre para saber si ya existen

			qr = planes.objects.filter(CodigoPlan=cp)
			qr2= planes.objects.filter(Nombre=cp2)	
			if qr.exists():
				mensaje="El CodigoPlan ya existe"
				return render(request,template,locals(),context_instance=RequestContext(request))

			if qr2.exists():
				mensaje="Nombre de Plan Existente"
				return render(request,template,locals(),context_instance=RequestContext(request))

			#Asigno variables que vienen del form a el modelo.
			plan.CodigoPlan = request.POST.get("CodigoPlan","")
			plan.Nombre = request.POST.get("Nombre","")

			#salvo los datos anteriores y se ingresan a la bd
			plan.save()
			#Despues de salvar se va al return render y queda en la misma url del form.

	else:
		form = planesForm

	return render(request, 'plan.html', {'form': form})


@login_required
def set_asesores(request):
	if request.method=='POST':
		form=asesorForm(request.POST)

		if form.is_valid():
			asesor=asesores()

			
			asesor.NombreAsesor = request.POST.get("NombreAsesor","")

			asesor.save()
		
	else:
		form = asesorForm()
		
	return render(request, 'asesores.html', {'form': form})

@login_required
def upt_planes(request):
	q= planes.objects.all()
	template='modificar.html'
	if request.method=='POST':
		val=planes.objects.filter(pk=request.POST.get("id","")).update(Nombre=request.POST.get("nombre",""))
		

	return render(request,template,locals(),context_instance=RequestContext(request))


@login_required
def upd_guia(request):
	q= suscripcion.objects.all()
	qr=tiraje.objects.all()
	template='guia.html'
	if request.method=='POST':
		val=planes.objects.filter(pk=request.POST.get("Codigo","")).update(Suscriptor=request.POST.get("Suscriptor",""))

	return render(request,template,locals(),context_instance=RequestContext(request))

@login_required
def set_clientes(request):
	q=departamentos.objects.filter(pk=request.POST.get(id,))
	if request.method=='POST':
		form=clientesForm(request.POST)
		
		if form.is_valid():
			
			form.save()
		
	else:
		form=clientesForm()

	return render(request, 'NewClient.html', {'form': form})

@login_required
def set_control(request):
	if request.method=='POST':
		form=controlForm(request.POST)

		if form.is_valid():
			c=control()

			c.codigo=request.POST.get("Control","")
			c.fecha=request.POST.get("Fecha","")
			c.supervisor=request.POST.get("Supervisor","")
			c.opcion=request.POST.get("Opcion","")
			c.comentarios=request.POST.get("Comentarios","")

			cliente.save()
	else:
		form=controlForm()

	return render(request, 'control.html', {'form': form})

@login_required
def set_suscripcion(request):
	if request.method=='POST':
		form=suscripcionForm(request.POST)
		fr=guiaForm(request.POST)
		f=
		if form.is_valid():

			g=guia()

			g.Fecha=request.POST.get("Fecha","")
			g.Ruta=request.POST.get("Ruta","")
			g.Supervisor=request.POST.get("Supervisor","")
			g.Cliente=request.POST.get("Cliente","")
			g.Destino=request.POST.get("De")
			Envios
			Cortesias
			Suscripciones

			form.save()

	else:
		form=suscripcionForm()

	return render(request, 'suscripciones.html',{'form': form})

@login_required
def set_empleados(request):
	if request.method=='POST':
		form=empleadosForm(request.POST)

		if form.is_valid():

			form.save()
	else:
		form=empleadosForm()

	return render (request, 'empleado.html', {'form': form})

@login_required
def set_cierre(request):
	cr= suscripcion.objects.all()
	template='cierre.html'
	if request.method=='POST':
		s=suscripcion.objects.filter(pk=request.POST.get("Codigo","")).update(Suscriptor=request.POST.get("Suscriptor",""))

	return render(request,template,locals(),context_instance=RequestContext(request))

@login_required
def set_factura(request):
	f = suscripcion.objects.all()
	template = 'factura.html'
