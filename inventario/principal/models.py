from django.db import models

# Create your models here.
class ElementoHardware(models.Model):
	numeroSerie = models.CharField(max_length = 50)
	nombre =  models.CharField(max_length = 100)
	observaciones = models.TextField()

	def __unicode__(self):
		return self.nombre
	
	
		
		