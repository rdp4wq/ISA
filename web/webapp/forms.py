from django import forms
from django.db import models
from django.forms import PasswordInput, extras
from django.core.validators import RegexValidator

basicValidator = RegexValidator(
    regex='^[ a-zA-Z]*$',
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
# dobValidator = RegexValidator(
#     regex='^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])+$',
#     message='Please enter YYYY-MM-DD',
#     code='invalid_DOB'
# )


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, validators=[usernameValidator])
    password = forms.CharField(label='Password', max_length=100, validators=[passwordValidator], widget=PasswordInput())


USER_TYPE = (
    ('Daddy', 'Daddy'),
    ('Baby', 'Baby')
)

class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, validators=[basicValidator])
    last_name = forms.CharField(label='Last Name', max_length=100, validators=[basicValidator])
    email = forms.CharField(label='Email', max_length=100, validators=[emailValidator])
    username = forms.CharField(label='Username', max_length=100, validators=[usernameValidator])
    password = forms.CharField(label='Password', max_length=100, validators=[passwordValidator], widget=PasswordInput())
    date_of_birth = forms.CharField(label="Date of Birth (YYYY-MM-DD)")
    city = forms.CharField(label='City', max_length=100, validators=[basicValidator])
    state = forms.CharField(label='State', max_length=100, validators=[basicValidator])
    user_type = forms.ChoiceField(label='Are you a...', choices=USER_TYPE)
    income = forms.IntegerField(label='Income', required=False)

class DateForm(forms.Form):
    user = forms.IntegerField(initial=3, required=False)
    price = forms.IntegerField(label='Price')
    description = forms.CharField(label='Description')
