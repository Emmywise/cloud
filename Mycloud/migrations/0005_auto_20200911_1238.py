# Generated by Django 3.0.7 on 2020-09-11 11:38

import Mycloud.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycloud', '0004_auto_20200911_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to=Mycloud.models.user_directory_path),
        ),
    ]
