from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ("name", "image", "description")

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': "form-control"})
        
        self.fields['description'].widget.attrs.update({'rows': "3"})
