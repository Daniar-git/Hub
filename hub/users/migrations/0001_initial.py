# Generated by Django 4.1.5 on 2023-01-30 13:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(6)])),
            ],
        ),
    ]
