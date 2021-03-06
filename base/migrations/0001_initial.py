# Generated by Django 2.1 on 2019-03-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default=None, max_length=48, null=True)),
                ('request_value', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Пошуковий запит',
                'verbose_name_plural': 'Пошукові запити',
                'ordering': ['-created'],
            },
        ),
    ]
