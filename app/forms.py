from django import forms
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm
from .models import Users

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Users  # Cambiado aquí
        #exclude = ['RegistrationDate', 'Biography', 'PerfilPhoto']  # Excluye el campo no editable        
        fields = UserCreationForm.Meta.fields + ('Name', 'Last_name', 'Username', 'Email', 'Gener', 'Ubication')

=======
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'gender', 'location']
        widgets = {
            'gender': forms.Select(choices=CustomUser.gender_choices),
        }
>>>>>>> master
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
<<<<<<< HEAD
        return password2
=======
        return password2        
>>>>>>> master
