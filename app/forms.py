from django import forms
from app.models import *
class insertForm(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = '__all__'