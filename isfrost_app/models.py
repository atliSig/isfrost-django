import datetime
from django.db import models
from django.utils import timezone

class ProductCategory(models.Model):
	category_name = models.CharField('Product category name', max_length=200)
	pub_date = models.DateTimeField('Date published', default = timezone.now)
	def __str__(self):
		return self.category_name

class Product(models.Model):
	product_name = models.CharField('Product name', max_length=200)
	pub_date = models.DateTimeField('Date published', default = timezone.now)
	product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, default=1)
	product_text = models.TextField('About product', default='Engar nánari upplýsingar')
	product_price = models.IntegerField('Product price', default=0)

	def __str__(self):
		return self.product_name
	def is_new(self):
		now = timezone.now()
		return  now - datetime.timedelta(days=30) <= self.pub_date <= now

class ServiceCategory(models.Model):
	category_name = models.CharField('Service category name', max_length=200)
	pub_date = models.DateTimeField('Date published', default = timezone.now)
	def __str__(self):
		return self.category_name

class Service(models.Model):
	service_name = models.CharField('Service name', max_length=200)
	pub_date = models.DateTimeField('Date published', default = timezone.now)
	service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, default=1)
	def __str__(self):
		return self.service_name