from asyncio.windows_events import NULL
from pyexpat import model
from django.db import models

# Create your models here.

def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])

class studentproject(models.Model):
    projectname=models.CharField(max_length=80)
    projectfile=models.FileField(default=0,upload_to='media/')

    def __str__(self):
        return self.projectname
