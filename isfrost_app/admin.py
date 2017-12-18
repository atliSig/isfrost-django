"""The admin condfiguration for the isfrost_app app"""
from django.contrib import admin
from .models import Product, ProductCategory, Service, ServiceCategory, Staff, Article, Company, IndexPage

class ProductCategoryAdmin(admin.ModelAdmin):
    """An admin model wrapper for the ProductCategory model"""
    fields = ['category_name', 'category_description', 'category_image', 'admin_img', 'pub_date']
    readonly_fields = ['admin_img']

class ProductAdmin(admin.ModelAdmin):
    """An admin model wrapper for the Product model"""
    fields = ['pub_date', 'product_name', 'product_category']

class ServiceCategoryAdmin(admin.ModelAdmin):
    """An admin model wrapper for the ServiceCategory model"""
    fields = ['category_name', 'category_description', 'category_icon', 'admin_icon', 'pub_date']
    readonly_fields = ['admin_icon']

class StaffAdmin(admin.ModelAdmin):
    """An admin model wrapper for the Staff model"""
    fields = ['name', 'email', 'phone', 'image', 'admin_img', 'pub_date']
    readonly_fields = ['admin_img']

class ArticleAdmin(admin.ModelAdmin):
    """An admin model wrapper for the Article model"""
    fields = ['title', 'subtitle', 'text', 'image', 'admin_img', 'pub_date']
    readonly_fields = ['admin_img']

class IndexPageAdmin(admin.ModelAdmin):
    """An admin model wrapper for the Index page model"""
    fields = ['introduction', 'cover_image', 'admin_img']
    readonly_fields = ['admin_img']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Service)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Company)
admin.site.register(IndexPage, IndexPageAdmin)
