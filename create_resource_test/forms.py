from django import forms
from create_resource_test.models import ResourceTest, Language, Framework, Database, Technology

class ResourceTestForm(forms.ModelForm):
    class Meta:
        model = ResourceTest
        fields = ('name', 'link', 'attachment', 'attachment', 'language', 'framework', 'database', 'technology')
        # languages = ModelChoiceField(queryset=Language.objects.all())
        # frameworks = ModelChoiceField(queryset=Framework.objects.all())
        # databases = ModelChoiceField(queryset=Database.objects.all())
        # technologys = ModelChoiceField(queryset=Technology.objects.all())

