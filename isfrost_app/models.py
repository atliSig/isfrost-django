"""The model configuration for the isfrost_app app"""
import datetime
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

class ProductCategory(models.Model):
    """The ProductCategory model class"""
    category_name = models.CharField('Nafn vöruflokks', max_length=200)
    pub_date = models.DateTimeField('Búið til þann', default=timezone.now)
    category_image = models.ImageField(upload_to='images/product_categories/%Y/%m', null=True)
    category_description = models.TextField('Um vöruflokk', default='Engar nánari upplýsingar')
    def __str__(self):
        return self.category_name
    def admin_img(self):
        """Returns a markup block to display image in admin view"""
        return mark_safe('<img src="%s"/>' % self.category_image.url)
    admin_img.allow_tags = True
    admin_img.short_description = 'Valin mynd'

class Product(models.Model):
    """The Product model class"""
    product_name = models.CharField('Product name', max_length=200)
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, default=1)
    product_text = models.TextField('About product', default='Engar nánari upplýsingar')
    product_price = models.IntegerField('Product price', default=0)
    product_image = models.FileField(upload_to='images/products/%Y/%m', null=True)

    def __str__(self):
        return self.product_name
    def is_new(self):
        """Returns true if object was created in the last 30 days"""
        now = timezone.now()
        return  now - datetime.timedelta(days=30) <= self.pub_date <= now

class ServiceCategory(models.Model):
    """The Service category model class"""
    category_name = models.CharField('Service category name', max_length=200)
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    category_description = models.TextField('Um vöruflokk', default='Engar nánari upplýsingar')
    category_icon = models.CharField('tákn', max_length=20, null=True, help_text="1. Finna tákn hér: http://fontawesome.io/icons/ 2. Láta inn nafn, t.d. \"address-book\"")
    def admin_icon(self):
        """Returns a markup block to display icon in admin view"""
        return mark_safe('<span><i class="fa fa-%s"></i></span>' % self.category_icon)
    admin_icon.allow_tags = True
    admin_icon.short_description = 'Valið tákn'
    def __str__(self):
        return self.category_name

class Service(models.Model):
    """The Service model class"""
    service_name = models.CharField('Service name', max_length=200)
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, default=1)
    service_text = models.TextField('About service', default='Engar nánari upplýsingar')
    def __str__(self):
        return self.service_name
