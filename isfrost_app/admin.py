from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'product_name', 'product_category']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(Service)
admin.site.register(ServiceCategory)
