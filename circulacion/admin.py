from django.contrib import admin
from circulacion.models import *

# Register your models here.

class PlanesAdmin(admin.ModelAdmin):
	list_display = ('CodigoPlan','Nombre')

class DeptoAdmin(admin.ModelAdmin):
	pass

class ClienteAdmin(admin.ModelAdmin):
	ordering = ['Codigo','Nombre']
	list_display =('Codigo','Nombre')

class CiudadAdmin(admin.ModelAdmin):
	pass

class AsesorAdmin(admin.ModelAdmin):
	ordering = ['id','NombreAsesor']

class SupervisorAdmin(admin.ModelAdmin):
	pass

class guiaAdmin(admin.ModelAdmin):
	pass

class rutaAdmin(admin.ModelAdmin):
	pass

class SuscripcionesAdmin(admin.ModelAdmin):
	ordering = ['Codigo','Suscriptor']
	list_display =('Codigo','Suscriptor')


class RepartidoresAdmin(admin.ModelAdmin):
	pass

class empleadosAdmin(admin.ModelAdmin):
	pass

class tirajeAdmin(admin.ModelAdmin):
	ordering=['id']
	list_display=('lunes','martes','miercoles','jueves','viernes','sabado','domingo')

admin.site.register(asesores,AsesorAdmin)
admin.site.register(ciudades,CiudadAdmin)
admin.site.register(clientes,ClienteAdmin)
admin.site.register(departamentos,DeptoAdmin)
admin.site.register(empleados,empleadosAdmin)
admin.site.register(guia,guiaAdmin)
admin.site.register(planes,PlanesAdmin)
admin.site.register(repartidores,RepartidoresAdmin)
admin.site.register(rutas,rutaAdmin)
admin.site.register(supervisores,SupervisorAdmin)
admin.site.register(suscripcion,SuscripcionesAdmin)
admin.site.register(tiraje,tirajeAdmin)