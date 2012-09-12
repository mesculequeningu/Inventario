# Create your views here.

from principal.models import ElementoHardware
from principal.forms import ElementoHardwareForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def lista_ElementosHardware(request):
	elementoshardware = ElementoHardware.objects.all()
	return render_to_response('lista_elementoshardware.html',{'lista':elementoshardware})

def nuevo_elementohardware(request):
	if request.method=='POST':
		formulario = ElementoHardwareForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = ElementoHardwareForm()
	return render_to_response('elementohardwareform.html',{'formulario':formulario}, context_instance = RequestContext(request)) 