from django import forms
from django.forms import ModelForm
from circulacion.models import *

class planesForm(forms.Form):
	CodigoPlan= forms.CharField(label='Codigo Plan')
	Nombre=forms.CharField(label='Nombre del Plan')

class asesorForm(forms.ModelForm):
	class Meta:
		model=asesores
		fields=['NombreAsesor']
	

class clientesForm(forms.ModelForm):
	class Meta:
	   model = clientes
	   fields= '__all__'
	    
class controlForm(forms.ModelForm):
    class Meta:
        model = control
        fields = '__all__'

class suscripcionForm(forms.ModelForm):
    class Meta:
        model = suscripcion
        fields = '__all__'

class empleadosForm(forms.ModelForm):
	class Meta:
		model = empleados
		fields = '__all__'

class cierreForm(forms.ModelForm):
    class Meta:
        model = cierre
        fields ='__all__'

class guiaForm(forms.ModelForm):
    class Meta:
        model = guia
        fields='__all__'
        
class tirajeForm(forms.ModelForm):
        class Meta:
            model = tiraje
            fields='__all__'
    