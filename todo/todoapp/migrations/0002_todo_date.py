# Generated by Django 3.2.7 on 2021-09-30 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateField(default='1999-01-01'),
            preserve_default=False,
        ),
    ]
