from django.db import models
from django.contrib.auth.models import User

from categories.views import VideoCategory

#-------------------------------------------------------------------------------

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    category = models.ForeignKey(VideoCategory, blank=True, null=True, default=None, on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length=500, blank=False)
    url = models.URLField(max_length=500, blank=False)
    yt_id = models.CharField(max_length=500, blank=True)
    start = models.FloatField(default = 0)
    end = models.FloatField(default = 0)
    def __str__(self):
        return self.title;
        
#-------------------------------------------------------------------------------        
