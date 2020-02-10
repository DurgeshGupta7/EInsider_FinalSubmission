#importing form from django and extending the functionality using meta class
from django import forms
#imported File table from models.py of same app
from .models import File

class FileForm(forms.ModelForm):
	class Meta:
		model = File
		fields = ('title','file_type','file')