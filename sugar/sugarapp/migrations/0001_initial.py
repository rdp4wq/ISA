# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('first_name', models.TextField(max_length=50)),
                ('last_name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Daddy',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('first_name', models.TextField(max_length=50)),
                ('last_name', models.TextField(max_length=50)),
            ],
        ),
    ]
