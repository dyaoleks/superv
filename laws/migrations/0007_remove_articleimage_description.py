# Generated by Django 2.1 on 2019-03-14 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0006_auto_20190314_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleimage',
            name='description',
        ),
    ]