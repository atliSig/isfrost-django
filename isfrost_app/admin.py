"""The admin condfiguration for the isfrost_app app"""
from django.contrib import admin
from .models import Product, ProductCategory, Service, ServiceCategory

class ProductCategoryAdmin(admin.ModelAdmin):
    """An admin model wrapper for the ProductCategory model"""
    fields = ['category_name', 'category_description', 'category_image', 'admin_img', 'pub_date']
    readonly_fields = ['admin_img']

class ProductAdmin(admin.ModelAdmin):
    """An admin model wrapper for the Product model"""
    fields = ['pub_date', 'product_name', 'product_category']

class ServiceCategoryAdmin(admin.ModelAdmin):
    """An admin model wrapper for the ServiceCategory model"""
    fields = ['category_name', 'category_description', 'category_icon','admin_icon', 'pub_date']
    readonly_fields = ['admin_icon']
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Service)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
