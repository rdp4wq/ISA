from django.db import models

# Create your models here.
class Baby(models.Model):
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)

class Daddy(models.Model):
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)