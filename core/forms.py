from django import forms
from .models import User, Project

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class AssociateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['users']
        widgets = {
            'users': forms.CheckboxSelectMultiple()
        }
