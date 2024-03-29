from django import forms
from .models import Gist,Comment

class GistForm(forms.ModelForm):
    class Meta:
        model = Gist
        fields = ('title','description','is_private','file')
