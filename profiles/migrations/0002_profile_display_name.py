# Generated by Django 5.0.6 on 2024-06-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='display_name',
            field=models.BooleanField(default=False),
        ),
    ]