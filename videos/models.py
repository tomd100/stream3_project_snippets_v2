from django.db import models
from django.core.validators import *
from django.contrib import auth, messages

# Create your models here.

#-------------------------------------------------------------------------------

class Video(models.Model):
    user = models.ForeignKey('auth.User')
    category = models.CharField(max_length=500, blank=True)
    title = models.CharField(max_length=500, blank=False)
    url = models.URLField(max_length=500, blank=False)
    yt_id = models.URLField(max_length=500, blank=True)
    start = models.FloatField(default = 0)
    end = models.FloatField(default = 0)
    
    def __str__(self):
        return self.title;
        
#-------------------------------------------------------------------------------        

