# Generated by Django 3.0.7 on 2020-09-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycloud', '0020_auto_20200924_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=models.ImageField(upload_to='images/%y%m%d'),
        ),
    ]
