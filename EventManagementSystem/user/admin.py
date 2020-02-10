from django.contrib import admin
#from same class models importing Profile model
from .models import Profile

# Register your models here.

admin.site.register(Profile)
