# Generated by Django 2.1 on 2019-03-14 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0005_auto_20190314_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr_is_active', models.BooleanField(default=True)),
                ('descr_name', models.TextField(blank=True, default=None, max_length=2048, null=True)),
                ('law_title', models.CharField(blank=True, default=None, max_length=1024, null=True)),
                ('law_chapter', models.CharField(blank=True, default=None, max_length=128, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='objecttype',
            name='descr_is_active',
        ),
        migrations.RemoveField(
            model_name='objecttype',
            name='descr_name',
        ),
        migrations.RemoveField(
            model_name='objecttype',
            name='law_chapter',
        ),
        migrations.RemoveField(
            model_name='objecttype',
            name='law_title',
        ),
        migrations.AddField(
            model_name='description',
            name='objecttype',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='laws.ObjectType'),
        ),
        migrations.AddField(
            model_name='articleimage',
            name='description',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='laws.Description'),
        ),
    ]
