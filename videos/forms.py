from django.forms import ModelForm
from .models import Video, VideoCategory

#-------------------------------------------------------------------------------

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'url']

#-------------------------------------------------------------------------------

# class VideoCategoryForm(ModelForm):
#     class Meta:
#         model = VideoCategory
#         fields = ['category']
        
#-------------------------------------------------------------------------------        