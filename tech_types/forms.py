from django import forms
from create_resource_test.models import Language, Framework, Database, Technology

class NewLanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ('language',)

class NewFrameworkForm(forms.ModelForm):
    class Meta:
        model = Framework
        fields = ('framework',)


class NewDatabaseForm(forms.ModelForm):
    class Meta:
        model = Database
        fields = ('database',)


class NewTechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ('technology',)