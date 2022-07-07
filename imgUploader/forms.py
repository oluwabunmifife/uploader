from django import forms
from django.forms import ModelForm
from . import models

class ImageForm(ModelForm):
    class Meta:
        model = models.Images
        fields = (
            'file', 'name', 'description',
        )
        widget = {
            "file": forms.ClearableFileInput(attrs={'type':'file','class': 'form-control', 'placeholder': "Upload Image"})
            
        }
