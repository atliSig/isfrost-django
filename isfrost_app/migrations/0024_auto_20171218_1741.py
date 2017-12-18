# Generated by Django 2.0 on 2017-12-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isfrost_app', '0023_auto_20171218_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='cover_image',
            field=models.ImageField(null=True, upload_to='images/company/%Y/%m', verbose_name='Forsíðumynd'),
        ),
        migrations.AddField(
            model_name='company',
            name='hours_week',
            field=models.CharField(default='08-18 alla virka daga', max_length=200, verbose_name='Opnunartími virkra daga'),
        ),
        migrations.AddField(
            model_name='company',
            name='hours_weekends',
            field=models.CharField(default='Lokað um helgar', max_length=200, verbose_name='Opnunartími helga'),
        ),
        migrations.AddField(
            model_name='company',
            name='loc_x',
            field=models.CharField(default='362464', max_length=6, verbose_name='X staðsetningar'),
        ),
        migrations.AddField(
            model_name='company',
            name='loc_y',
            field=models.CharField(default='405894', max_length=6, verbose_name='Y staðsetningar'),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(default='isfrost@isfrost.is', max_length=254, verbose_name='póstur'),
        ),
    ]
