# Generated by Django 4.2 on 2024-12-19 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sellers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='profile_pictures/'),
        ),
    ]