from django.db import models


#-------------------------------------------------------------------------------        

class VideoCategory(models.Model):
    category = models.CharField(max_length=500, blank=False)
    def __str__(self):
        return self.category;
        
#-------------------------------------------------------------------------------        