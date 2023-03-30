from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import widgets

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'is_active' , 'username','nama', 'password1','password2')

        widgets = {
            'email' : forms.TextInput(attrs={
                'class':'input100 email'
            }),
            'is_active' : forms.HiddenInput(),
            'nama' : forms.TextInput(attrs={
                'class':'input100',
            }),
            'username' : forms.TextInput(attrs={
                'class':'input100'
            }),
            'password1' : forms.PasswordInput(attrs={
                'class':'input100'
            }),
            'password2' : forms.PasswordInput(attrs={
                'class':'input100'
            }),
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "p-2 mt-8 rounded-lg border",
                "placeholder":"Username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "p-2 rounded-lg border w-full",
                "placeholder":"Password",
            }
        )
    )

class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "input100"
            }
        )
    )
    reconfirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input100"
            }
        )
    )

class ProfilForm(forms.Form):
    new_password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "input100"
            }
        )
    )
    reconfirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input100"
            }
        )
    )

class EmailForm(forms.Form):
    email = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "input100"
            }
        )
    )