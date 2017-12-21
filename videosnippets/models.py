from django.db import models
from django.core.validators import *
from django.contrib import auth, messages
from videos.models import Video

#-------------------------------------------------------------------------------    
    
class Snippet(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=False)
    start = models.FloatField(blank=True, default = 0)
    end = models.FloatField(blank=True, default = 0)
    jump = models.FloatField(blank=True, default = 2)
    
    def __str__(self):
        return self.title;
        
#-------------------------------------------------------------------------------
