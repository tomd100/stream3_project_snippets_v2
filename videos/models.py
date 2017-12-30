from django.db import models

from categories.views import VideoCategory

#-------------------------------------------------------------------------------

class Video(models.Model):
    user = models.ForeignKey('auth.User')
    category = models.ForeignKey(VideoCategory, on_delete=models.SET_DEFAULT, default='General')
    # category = models.CharField(max_length=500, blank=True)
    title = models.CharField(max_length=500, blank=False)
    url = models.URLField(max_length=500, blank=False)
    yt_id = models.URLField(max_length=500, blank=True)
    start = models.FloatField(default = 0)
    end = models.FloatField(default = 0)
    def __str__(self):
        return self.title;
        
#-------------------------------------------------------------------------------        
