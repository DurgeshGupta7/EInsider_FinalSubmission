#importing forms from django
from django import forms
#importing models List from models.py of same project
from .models import List

#using meta class to extend the functionality of existing class
class ListForm(forms.ModelForm):
	class Meta:
		model = List
		# fields used to show the details in client side in same order
		fields= ["item", "completed"]