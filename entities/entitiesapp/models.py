from django.db import models
from entities.settings import SECRET_KEY
import hmac
import os

us_states = (
    ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),
    ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'),
    ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'),
    ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
    ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'),
    ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'),
    ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
    ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'),
    ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')
)

# Create your models here.


class User(models.Model):
    user_types = (
        ('Daddy', 'Daddy'),
        ('Baby', 'Baby'),
    )
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.TextField(null=False, blank=False)
    user_type = models.CharField(max_length=5, choices=user_types, null=False, blank=False)
    date_created = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField()
    income = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=2, choices=us_states, null=False, blank=False)


class Authenticator(models.Model):
    user = models.OneToOneField(User, null=False)
    authenticator = models.CharField(max_length=64, null=False, primary_key=True)
    date_created = models.DateField(auto_now_add=True)


class Date(models.Model):
    user = models.ForeignKey(User, null=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
