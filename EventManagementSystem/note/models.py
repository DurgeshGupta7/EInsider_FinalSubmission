from django.db import models
#imported User model from django.contrib.auth to create foreign key relation
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)

	def _str_(self):
		return self.item + ' | ' + str(self.completed)
 

