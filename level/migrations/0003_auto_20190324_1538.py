# Generated by Django 2.1 on 2019-03-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0002_auto_20190323_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='name',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]
