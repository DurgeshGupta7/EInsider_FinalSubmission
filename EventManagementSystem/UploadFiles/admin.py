from django.contrib import admin
#imported File table from same app
from .models import File

# Register your models here.

admin.site.register(File)
