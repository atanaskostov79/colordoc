# Generated by Django 4.0.4 on 2022-05-10 17:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(['doc', 'docx'])]),
        ),
    ]