from django import forms
from .models import Form1


class Mform1(forms.ModelForm):
    class Meta:
        model = Form1
        fields = '__all__'


