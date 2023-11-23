from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # Cambiado aquí
        #exclude = ['RegistrationDate', 'Biography', 'PerfilPhoto']  # Excluye el campo no editable        
        fields = UserCreationForm.Meta.fields + ('Name', 'Last_name', 'Username', 'Email', 'Gener', 'Ubication')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2
