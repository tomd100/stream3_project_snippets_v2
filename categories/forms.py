from django.forms import ModelForm
from .models import VideoCategory

#-------------------------------------------------------------------------------

class VideoCategoryForm(ModelForm):
    class Meta:
        model = VideoCategory
        fields = ['category']
        
#-------------------------------------------------------------------------------        