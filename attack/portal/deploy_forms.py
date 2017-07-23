from django import forms
from .models import Portal

class PostForm(forms.ModelForm):
    class Meta:
            model = Portal
            fields
