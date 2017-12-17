# Generated by Django 2.0 on 2017-12-15 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isfrost_app', '0008_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_image',
            field=models.FileField(null=True, upload_to='images/product_categories/%Y/%m'),
        ),
    ]
