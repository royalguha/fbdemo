# Generated by Django 2.1 on 2020-06-05 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbapp', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='pics/defaultmale.jpg', upload_to='pics'),
        ),
    ]
