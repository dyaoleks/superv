# Generated by Django 2.1 on 2019-03-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchrequest',
            name='total_results',
            field=models.CharField(blank=True, default=None, max_length=8, null=True),
        ),
    ]
