# Generated by Django 3.0.7 on 2020-09-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycloud', '0005_auto_20200911_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/%Y/%m/%d/'),
        ),
    ]
