# Generated by Django 2.1 on 2019-03-14 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0003_auto_20190314_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='objecttype',
        ),
        migrations.AddField(
            model_name='objecttype',
            name='description',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='laws.Description'),
        ),
    ]