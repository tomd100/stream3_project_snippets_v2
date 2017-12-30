from django.forms import ModelForm, TextInput
from .models import Snippet
from django import forms


#-------------------------------------------------------------------------------
        
class SnippetSaveForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'start', 'end', 'jump']        

#-------------------------------------------------------------------------------        