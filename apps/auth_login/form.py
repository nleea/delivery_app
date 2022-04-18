from time import clock_getres
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import EmailValidator
# from django.core.validators import MinLengthValidator
# from django.forms import ModelForm


class FormsAuthentication(AuthenticationForm):
    # username = forms.CharField(max_length=20, validators=[
    #                            MinLengthValidator(5)])
    # password = forms.CharField(
    #     max_length=30, validators=[MinLengthValidator(10)])

    class Meta:
        model = AuthenticationForm
        fields = ('username', 'password')

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                message='This account is inactive.',
                code='inactive'
            )
        return user


class AuthForms(UserCreationForm, forms.ModelForm):
    email = forms.EmailField(max_length=250,
                             validators=[EmailValidator('No es un correo verifique')])
    firts_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    password1 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['email', 'firts_name', 'last_name', 'password1', 'password2']

    def clean(self):
        clean = super().clean()
        if User.objects.filter(email=clean['email']):
            self.add_error('email', 'Ya existe este email')
        return clean
