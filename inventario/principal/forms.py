from django.forms import ModelForm
from principal.models import ElementoHardware

class ElementoHardwareForm(ModelForm):
	"""docstring for ElementoHardware"""
	class Meta:
		model = ElementoHardware


