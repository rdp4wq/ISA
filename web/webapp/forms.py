from django import forms

class LoginForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class RegisterForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)