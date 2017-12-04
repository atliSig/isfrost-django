import datetime
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from .models import Product

def create_product(product_name, days):
	'''
	Creates a new product with product_name of 'product_name' and
	pub_date of now with the offset of 'days', positive for future
	negative for past offsets
	'''
	time = timezone.now() + datetime.timedelta(days=days)
	return Product(product_name=product_name, pub_date = time)

class IndexViewTests(TestCase):
	def test_no_products(self):
		'''
		If no products, a message is displayed
		'''
		response = self.client.get(reverse('main:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No products are available")
		self.assertQuerysetEqual(response.context['latest_products'], [])

class ProductModelTests(TestCase):
	def test_is_new_on_future_product(self):
		'''
		is_new() returns False for products whose pub_date
		is in the future
		'''
		time = timezone.now() + datetime.timedelta(days=30)
		future_product = Product(pub_date = time)
		self.assertIs(future_product.is_new(), False)
	def test_is_new_on_past_product(self):
		'''
		is_new returns False for products whose pub_date
		is more than 30 days in the past
		'''
		time = timezone.now() - datetime.timedelta(days=31)
		past_product = Product(pub_date = time)
		self.assertIs(past_product.is_new(), False)
	def test_is_new_on_recent_product(self):
		'''
		is_new returns True for products whose pub_date
		is not in future and at most 30 days old
		'''
		time = timezone.now() - datetime.timedelta(days=30)
		current_product = Product(pub_date = time)
		self.assertIs(current_product.is_new(), True)