from django import forms
from .models import Project, BoardGroup, Board, Stage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ("name", "image", "description", "colour")
        widgets = {
            'colour': forms.TextInput(attrs={'type': 'color'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['description'].widget.attrs.update({'rows': "3"})
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Submit'))


class BoardGroupForm(forms.ModelForm):
    
    class Meta:
        model = BoardGroup
        fields = ("name", "project", "description", "colour")
        widgets = {
            'colour': forms.TextInput(attrs={'type': 'color'}),
        }

    def __init__(self, *args, **kwargs):
        super(BoardGroupForm, self).__init__(*args, **kwargs)
        
        self.fields['description'].widget.attrs.update({'rows': "3"})
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Submit'))


class BoardForm(forms.ModelForm):
    
    class Meta:
        model = Board
        fields = ("name", "project", "board_group", "image", "description", "colour")
        widgets = {
            'colour': forms.TextInput(attrs={'type': 'color'}),
        }

    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)
        
        self.fields['description'].widget.attrs.update({'rows': "3"})
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Submit'))


class StageForm(forms.ModelForm):
    
    class Meta:
        model = Stage
        fields = ("name", "description", "project", "board_group", "board", "order")
        widgets = {
            'project': forms.HiddenInput(),
            'board_group': forms.HiddenInput(),
            'board': forms.HiddenInput(),
            'order': forms.HiddenInput(),
        }
    
    def __init__(self, *args, **kwargs):
        super(StageForm, self).__init__(*args, **kwargs)
        
        self.fields['description'].widget.attrs.update({'rows': "3"})
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Submit'))
