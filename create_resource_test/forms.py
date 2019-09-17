from django import forms
from create_resource_test.models import ResourceTest, Language, Framework, Database, Technology

class ResourceTestForm(forms.ModelForm):
    class Meta:
        model = ResourceTest
        fields = ('name', 'link', 'attachment', 'attachment', 'language', 'framework', 'database', 'technology')
