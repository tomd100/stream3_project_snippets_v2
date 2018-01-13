from django.forms import ModelForm
from .models import Video
from categories.models import VideoCategory

#-------------------------------------------------------------------------------

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['category', 'url', 'title']
            
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None) 
        super(VideoForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = VideoCategory.objects.filter(user=request.user)

#-------------------------------------------------------------------------------
