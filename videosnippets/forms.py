from django.forms import ModelForm, TextInput
from .models import Snippet

#-------------------------------------------------------------------------------

# class SnippetForm(ModelForm):
    # title = models.CharField(
    #     widget = forms.TextInput(
    #         attrs = {'class': 'snippet_title'}
    #     )
    # );
    # start = forms.CharField(
    #     widget = forms.TextInput(
    #         attrs = {'class': 'snippet_markers', 'type':'number', 'step':'0.1'}
    #     )
    # );
    # end = forms.CharField(
    #     widget = forms.TextInput(
    #         attrs = {'class': 'snippet_markers', 'type':'number', 'step':'0.1'}
    #     )
    # );
    # jump = forms.CharField(
    #     widget = forms.TextInput(
    #         attrs = {'class': 'snippet_markers', 'type':'number', 'step':'0.1'}
    #     )
    # );
    
    # class Meta:
    #     model = Snippet
    #     fields = ['title', 'start', 'end', 'jump']

#-------------------------------------------------------------------------------
        
class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'start', 'end', 'jump']        
        widgets = {
            'title': TextInput(attrs = {'class': 'snippet_title'}),
            'start': TextInput(attrs = {'class': 'snippet_markers', 'type':'number', 'step':'0.1'}),
            'end': TextInput(attrs = {'class': 'snippet_markers', 'type':'number', 'step':'0.1'}),
            'jumo': TextInput(attrs = {'class': 'snippet_markers', 'type':'number', 'step':'0.1'}),
        }
        
#-------------------------------------------------------------------------------        