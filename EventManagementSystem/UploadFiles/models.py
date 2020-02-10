from django.db import models
#importing User model to create foreign key relation with File table
from django.contrib.auth.models import User


# Create your models here.

class File(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length = 100)
	file_type= models.CharField(max_length=100)
	file = models.FileField(upload_to='files/')

	def __str__(self):
		return self.title


	def delete(self,*args,**kwargs):
		self.file.delete()
		super().delete(*args,**kwargs)






