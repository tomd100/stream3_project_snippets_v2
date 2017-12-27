from django.forms import ModelForm, TextInput
from .models import Snippet


#-------------------------------------------------------------------------------
        
class SnippetDetailForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'start', 'end', 'jump']        
        widgets = {
            'start': TextInput(attrs = {'class': 'snippet_markers', 'type':'number', 'step':'0.1'}),
            'end': TextInput(attrs = {'class': 'snippet_markers', 'type':'number', 'step':'0.1'}),
            'jump': TextInput(attrs = {'class': 'snippet_markers', 'type':'number', 'step':'0.1'}),
        }
     
#-------------------------------------------------------------------------------        