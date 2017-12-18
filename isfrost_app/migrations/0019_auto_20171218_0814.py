# Generated by Django 2.0 on 2017-12-18 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('isfrost_app', '0018_auto_20171217_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nafn')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Búið til þann')),
                ('position', models.CharField(max_length=200, verbose_name='staða')),
                ('email', models.EmailField(max_length=200, verbose_name='Póstur')),
                ('phone', models.CharField(max_length=7, verbose_name='Símanúmer')),
                ('image', models.ImageField(null=True, upload_to='images/staff/%Y/%m')),
            ],
            options={
                'verbose_name': 'Starfsmaður',
                'verbose_name_plural': 'Starfsmenn',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Vara', 'verbose_name_plural': 'Vörur'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Vöruflokkur', 'verbose_name_plural': 'Vöruflokkar'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Þjónusta', 'verbose_name_plural': 'Þjónustur'},
        ),
        migrations.AlterModelOptions(
            name='servicecategory',
            options={'verbose_name': 'Þjónustuflokkur', 'verbose_name_plural': 'Þjónustuflokkar'},
        ),
    ]
