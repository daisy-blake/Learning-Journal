from django import forms
from models import Resource, LANGUAGE_CHOICES

class ResourceForm(forms.ModelForm):

    class Meta:
        model = Resource
        fields = ('name', 'link', 'attachment', 'attachment', 'language', 'framework', 'database', 'technology')







