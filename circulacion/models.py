from django.db import models
from django.contrib.auth.models import User

class planes(models.Model):
	CodigoPlan=models.CharField(max_length=4,primary_key=True)
	Nombre=models.CharField(max_length=50)
	

	def __str__(self):
		return self.CodigoPlan

	class Meta:
		ordering=['CodigoPlan']
		verbose_name_plural='Planes'

class supervisores(models.Model):
	Codigo=models.IntegerField(max_length=10,primary_key=True)
	Nombre=models.CharField(max_length=140)

	class Meta:
		verbose_name_plural='Supervisores'

	def __str__(self):
		return '%s - %s ' % (self.Codigo,self.Nombre)

class rutas(models.Model):
	NombreRuta=models.CharField(max_length=35,primary_key=True)
	Colonias=models.TextField()

	class Meta:
		ordering=['NombreRuta']
		verbose_name_plural="Rutas"

	def __str__(self):
		return self.NombreRuta

class asesores(models.Model):
	NombreAsesor=models.CharField(max_length=100)

	class Meta:
		ordering=['NombreAsesor']
		verbose_name_plural='Asesores'

	def __str__(self):
		return self.NombreAsesor

class repartidores(models.Model):
	NombreRepartidor=models.CharField(max_length=140)
	Telefono=models.CharField(max_length=10)

	class Meta:
		ordering = ['NombreRepartidor']
		verbose_name_plural='Repartidores'

	def __str__(self):
		return self.NombreRepartidor

class departamentos(models.Model):
	Departamentos=models.CharField(max_length=140)

	class Meta:
		verbose_name_plural='Departamentos'

	def __str__(self):
		return self.Departamentos

class ciudades(models.Model):
	Departamentos=models.ForeignKey(departamentos)
	Municipio=models.CharField(max_length=140)

	class Meta:
		ordering=['Departamentos']
		verbose_name_plural='Ciudades'

	def __str__(self):
		return self.Municipio

class control(models.Model):
	
	Opciones = (
		(1,'Faltaron X Vendedores'),
		(2,'Semaforo en mal Estado'),
		(3,'Falta de Energia Electrica'),
		(4,'Calle Cerrada'),
		(5,'Manifestacion')
		)

	codigo=models.IntegerField(max_length=10,primary_key=True)
	fecha=models.DateField()
	supervisor=models.ForeignKey(supervisores)
	opcion=models.CharField(max_length=140,choices=Opciones)
	comentarios=models.TextField(blank=True,null=True)

	class Meta:
		ordering=['fecha']
		verbose_name_plural='Hoja de Control'

	def __str__(self):
		return '%s - %s -%s' % (self.codigo,self.supervisor,self.opcion)

class clientes(models.Model):
	Codigo=models.IntegerField(max_length=10,primary_key=True)
	TipoCliente=models.CharField(max_length=50,choices=[('Empresarial','Empresarial'),('Residencial','Residencial')])
	Nombre=models.CharField(max_length=140)
	Identificacion=models.CharField(max_length=15)
	FechaNacimiento=models.DateField()
	Genero=models.CharField(max_length=15, blank=True, null=True ,choices=[('F','Femenino'),('M','Masculino')])
	Telefono=models.IntegerField(max_length=15)
	Celular=models.IntegerField(max_length=15,blank=True,null=True)
	Departamentos=models.ForeignKey(departamentos)
	Ciudad=models.ForeignKey(ciudades)
	Colonia=models.CharField(max_length=60)
	Calle=models.CharField(max_length=30)
	Avenida=models.CharField(max_length=30)
	Referencia=models.CharField(max_length=140)
	Correo=models.EmailField()
	latitud=models.CharField(max_length=50)
	longitud=models.CharField(max_length=50)

	class Meta:
		ordering=['Nombre']
		verbose_name_plural='Clientes'

	def __str__(self):
		return '%s - %s' % (self.Codigo,self.Nombre)

class repartidores(models.Model):
	NombreRepartidor=models.CharField(max_length=140)
	Telefono=models.CharField(max_length=10)

	class Meta:
		ordering=['NombreRepartidor']
		verbose_name_plural='Repartidores'

	def __str__(self):
		return self.NombreRepartidor

class suscripcion(models.Model):
	Codigo=models.IntegerField(max_length=10,primary_key=True)
	Suscriptor=models.ForeignKey(clientes)
	Empresa=models.CharField(max_length=50,choices=[('Empresarial','Empresarial'),('Residencial','Residencial')])
	Cantidad=models.IntegerField(max_length=5)
	Plan=models.ForeignKey(planes)
	Valor=models.DecimalField(max_digits=5,decimal_places=2)
	Contrato=models.IntegerField()
	Recibo=models.IntegerField()
	Asesor=models.ForeignKey(asesores)
	Ruta=models.ForeignKey(rutas)
	Entrega=models.CharField(max_length=4,choices=[('L-D','L-D'),('L-S','L-S'),('L-V','L-V')])
	Comentarios=models.CharField(max_length=140)
	Tipo=models.CharField(max_length=15,choices=[('Canje','Canje'),('Certificado','Certificado'),('Cortesia','Cortesia'),('DxP','DxP'),('Pagado','Pagado')])
	Inicio=models.DateField()
	Fin=models.DateField()
	Repartidor=models.ForeignKey(repartidores)


	class Meta:
		ordering=['Codigo','Suscriptor']
		verbose_name_plural='Suscripciones'

	def __str__(self):
		return '%s - %s' % (self.Codigo,self.Suscriptor)

class guia(models.Model):
    Fecha=models.DateField()
    Ruta= models.ForeignKey(rutas)
    Supervisor= models.ForeignKey(supervisores)
    Cliente=models.ForeignKey(clientes)
    Destino=models.CharField(max_length=140)
    Envios=models.IntegerField(max_length=5)
    Cortesias=models.IntegerField(max_length=5)
    Suscripciones=models.IntegerField(max_length=5)

    class Meta:
        ordering=['Ruta']
        verbose_name_plural = "Guía Producción"

    def __str__(self):
            pass  

class empleados(models.Model):
	Nombre=models.CharField(max_length=140)
	Puesto=models.CharField(max_length=140)

	class Meta:
		verbose_name_plural='Empleados'

	def __str__(self):
		return self.Nombre

class tiraje(models.Model):
	ruta=models.ForeignKey(rutas)
	lunes=models.IntegerField(max_length=5)
	martes=models.IntegerField(max_length=5)
	miercoles=models.IntegerField(max_length=5)
	jueves=models.IntegerField(max_length=5)
	viernes=models.IntegerField(max_length=5)
	sabado=models.IntegerField(max_length=5)
	domingo=models.IntegerField(max_length=5)

	class Meta:
		verbose_name_plural='Tiraje'

	def __str__(self):
		pass

class cierre(models.Model):
	Nombre=models.ForeignKey(suscripcion)
	Cantidad=models.IntegerField(max_length=5)
	Direccion=models.CharField(max_length=140)
	Tipo=models.ForeignKey(planes)
	Valor=models.DecimalField(max_digits=4, decimal_places=2)
	Recibo=models.CharField(max_length=10)
	ValorRecibo=models.DecimalField(max_digits=4,decimal_places=2)
	Comision=models.DecimalField(max_digits=4,decimal_places=2)
	FechaPago=models.DateField()
	Inicio=models.DateField()
	Fin=models.DateField()

class recibo(models.Model):
	Codigo=models.AutoField(primary_key=True)
	Fecha=models.DateField()
	Nombre=models.ForeignKey(clientes)
	Plan=models.ForeignKey(planes)
	Tipo=models.CharField(max_length=15,choices=[('Canje','Canje'),('Certificado','Certificado'),('Cortesia','Cortesia'),('DxP','DxP'),('Pagado','Pagado')])
	Descripcion=models.TextField()
	Valor=models.DecimalField(max_digits=5, decimal_places=2)


	class Meta:
		verbose_name_plural='Recibo'

	def __str__(self):
		return '%s - %s - %s' % (self.Codigo,self.Fecha,self.Nombre)





