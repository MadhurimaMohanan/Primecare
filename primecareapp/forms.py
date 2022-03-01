from django import forms
from .models import P_Contact

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = P_Contact
        fields = '__all__'