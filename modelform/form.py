from django import forms
from .models import Mform


class Mmform(forms.ModelForm):
    class Meta:
        model = Mform
        fields = '__all__'
        labels = {
            'first_name': "",
            'last_name': "",
            'email': "",

        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),


        }

