# Generated by Django 2.0 on 2017-12-24 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isfrost_app', '0029_auto_20171224_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(default='Engar nánari upplýsingar', null=True, verbose_name='Stutt lýsing um vöru'),
        ),
    ]
