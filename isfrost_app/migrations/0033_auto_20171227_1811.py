# Generated by Django 2.0 on 2017-12-27 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isfrost_app', '0032_auto_20171227_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['-name'], 'verbose_name': 'Starfsmaður', 'verbose_name_plural': 'Starfsmenn'},
        ),
    ]
