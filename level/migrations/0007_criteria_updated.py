# Generated by Django 2.1 on 2019-03-26 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0006_criteria_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='criteria',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
