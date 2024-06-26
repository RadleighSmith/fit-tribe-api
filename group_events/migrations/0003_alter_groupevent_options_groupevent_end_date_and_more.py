# Generated by Django 5.0.6 on 2024-06-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_events', '0002_eventmembership'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupevent',
            options={'ordering': ['-start_date', '-start_time'], 'verbose_name': 'Group Event', 'verbose_name_plural': 'Group Events'},
        ),
        migrations.AddField(
            model_name='groupevent',
            name='end_date',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='groupevent',
            name='start_date',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AlterField(
            model_name='groupevent',
            name='end_time',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='groupevent',
            name='start_time',
            field=models.TimeField(default='00:00:00'),
        ),
    ]
