from django.db import models
from django.contrib.auth.models import User

#-------------------------------------------------------------------------------        

class VideoCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    category = models.CharField(max_length=500, blank=False, default='')
    def __str__(self):
        return self.category;
        
#-------------------------------------------------------------------------------        