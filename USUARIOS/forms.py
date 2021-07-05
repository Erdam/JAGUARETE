from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    username = forms.CharField(
        label='Usuario', widget=forms.TextInput(), max_length=150, required=True, help_text='')
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(), max_length=30, required=True, help_text='Requerido. más 8 caracteres y no pueden ser todos numeros.')
    password2 = forms.CharField(
        label='Repetir Password', widget=forms.PasswordInput(), max_length=30, required=True, help_text='Requerido. Ingrese la misma contraseña que antes, para verificación.')
    first_name = forms.CharField(
        label='Nombre', widget=forms.TextInput(), max_length=30, required=False, help_text='')
    last_name = forms.CharField(
        label='Apellido', widget=forms.TextInput(), max_length=30, required=False, help_text='')
    email = forms.EmailField(
        label='Email', widget=forms.TextInput(), max_length=254, required=True, help_text='')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )