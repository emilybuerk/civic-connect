from .models import Template
from django import forms


class ScratchForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Name'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter description here'}),
        }

    def __init__(self, *args, **kwargs):
        super(TemplateForm, self).__init__(*args, **kwargs)
        name = kwargs.pop("name_placeholder")
        body = kwargs.pop("body_placeholder")
        self.fields['name'].placeholder = name
        self.fields['body'].placeholder = body
