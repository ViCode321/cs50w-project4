# Forms.py

from django import forms
from .models import Users

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['Name', 'Email', 'Gener', 'Password']  # Agrega otros campos si es necesario

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2
