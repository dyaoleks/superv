# Generated by Django 2.1 on 2019-03-18 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('norms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_name', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='norm_files/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_main', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Посилання на документ',
                'verbose_name_plural': 'Посилання на документи',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='normdock',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Нормативний документ', 'verbose_name_plural': 'Нормативні документи'},
        ),
        migrations.AddField(
            model_name='normdock',
            name='type',
            field=models.CharField(blank=True, default=None, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='normdock',
            name='name_code',
            field=models.CharField(max_length=24),
        ),
        migrations.AddField(
            model_name='links',
            name='normdock',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='norms.NormDock'),
        ),
    ]