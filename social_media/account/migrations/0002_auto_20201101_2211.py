# Generated by Django 3.0 on 2020-11-01 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='image',
            new_name='profile_image',
        ),
    ]
