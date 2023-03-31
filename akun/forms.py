from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import widgets

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
    label="Password",
    widget=forms.PasswordInput(attrs={'class':'p-2 rounded-lg border w-full', 'type':'password','placeholder':'Password'}),
    )
    password2 = forms.CharField(
    label="Password",
    widget=forms.PasswordInput(attrs={'class':'p-2 rounded-lg border w-full', 'type':'password','placeholder':'Konfirmasi password'}),
    )

    class Meta:
        model = User
        fields = ('email', 'is_active' , 'username')

        widgets = {
            'email' : forms.TextInput(attrs={
                'class':'p-2 rounded-lg border',
                'placeholder' : 'Email'
            }),
            'is_active' : forms.HiddenInput(),
            'username' : forms.TextInput(attrs={
                'class':'p-2 mt-4 rounded-lg border',
                'placeholder': 'Username'
            })
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "p-2 mt-4 rounded-lg border",
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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nama', 'email']

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['foto_profile']