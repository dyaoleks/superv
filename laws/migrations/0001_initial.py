# Generated by Django 2.1 on 2019-03-11 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products_images/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_main', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_description', models.TextField(max_length=2048)),
                ('law_title', models.CharField(blank=True, default=None, max_length=1024, null=True)),
                ('law_chapter', models.CharField(blank=True, default=None, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ObjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField()),
                ('headline', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='SupervChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SupervPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='objecttype',
            name='supervchapter',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='laws.SupervChapter'),
        ),
        migrations.AddField(
            model_name='objecttype',
            name='supervposition',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='laws.SupervPosition'),
        ),
        migrations.AddField(
            model_name='description',
            name='objecttype',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='laws.ObjectType'),
        ),
        migrations.AddField(
            model_name='articleimage',
            name='objecttype',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='laws.ObjectType'),
        ),
    ]
