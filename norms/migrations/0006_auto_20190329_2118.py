# Generated by Django 2.1 on 2019-03-29 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('norms', '0005_normdock_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='normdock',
            name='doc_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='normdock',
            name='doc_num',
            field=models.CharField(blank=True, default=None, max_length=8, null=True),
        ),
    ]