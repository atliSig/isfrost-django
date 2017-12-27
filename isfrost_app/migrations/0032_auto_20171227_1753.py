# Generated by Django 2.0 on 2017-12-27 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isfrost_app', '0031_auto_20171224_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.EmailField(max_length=200, null=True, verbose_name='Póstur'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone',
            field=models.CharField(max_length=7, null=True, verbose_name='Símanúmer'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.CharField(default='Almennur starfsmaður', max_length=200, verbose_name='Deild eða starfsheiti'),
        ),
    ]
