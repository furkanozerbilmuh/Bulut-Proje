from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'E-mail'}))
    password = forms.CharField(max_length=100,  widget=forms.PasswordInput(attrs={'placeholder' : 'Şifre'}))

class SignupForm(forms.ModelForm):


    class Meta:
        model = user
        fields = '__all__'

        widgets = {
            'f_name' : forms.TextInput(attrs={'placeholder' : 'İsim'}),
            'l_name' : forms.TextInput(attrs={'placeholder' : 'Soyisim'}),
            'email' : forms.EmailInput(attrs={'placeholder' : 'E-mail'}),
            'password' : forms.PasswordInput(attrs={'placeholder' : 'Şifre'}),
            'type' : forms.RadioSelect()
        }







