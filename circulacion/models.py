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