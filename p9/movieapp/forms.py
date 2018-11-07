from django import forms
from movieapp.models import movie

class movieForm(forms.ModelForm):
    class Meta:
        model=movie
        fields='__all__'