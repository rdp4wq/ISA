from django import forms
from django.forms import PasswordInput
from django.core.validators import RegexValidator

basicValidator = RegexValidator(
    regex='^[a-zA-Z]*$',
    message='Input must only contain a-z, A-Z',
    code='invalid_input'
)
usernameValidator = RegexValidator(
    regex='^[a-zA-Z0-9]*$',
    message='Username must only contain a-z, A-Z, 0-9',
    code='invalid_username'
)
passwordValidator = RegexValidator(
    regex='^[a-zA-Z0-9@$!%*#?&]*$',
    message='Password must only contain a-z, A-Z, 0-9, @$!%*#?&',
    code='invalid_password'
)
emailValidator = RegexValidator(
    regex='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
    message='Invalid Email',
    code='invalid_email'
)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, validators=[usernameValidator])
    password = forms.CharField(label='Password', max_length=100, validators=[passwordValidator], widget=PasswordInput())


