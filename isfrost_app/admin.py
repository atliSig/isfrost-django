"""The admin condfiguration for the isfrost_app app"""
from django.contrib import admin
from .models import Product, ProductCategory, Service, ServiceCategory, Staff, Article, Company, IndexPage

def duplicate_action(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate_action.short_description = "Búa til afrit af völdum hlut"

class ProductCategoryAdmin(admin.ModelAdmin):
    """An admin model wrapper for the ProductCategory model"""
    fields = ['name', 'short_description', 'detailed_description', 'image', 'admin_img', 'pub_date']
    readonly_fields = ['admin_img']

class ProductAdmin(admin.ModelAdmin):
    """An admin model wrapper for the Product model"""
    fields = ['pub_date', 'name', 'product_category','short_description','detailed_description', 'price', 'image', 'admin_img']
    readonly_fields  = ['admin_img']
    list_display = ['name']
    actions = [duplicate_action]

class ServiceCategoryAdmin(admin.ModelAdmin):
    """An admin model wrapper for the ServiceCategory model"""
    fields = ['name', 'short_description', 'detailed_description', 'icon', 'admin_icon', 'pub_date']
    readonly_fields = ['admin_icon']

class StaffAdmin(admin.ModelAdmin):
    """An admin model wrapper for the Staff model"""
    fields = ['name', 'email', 'phone','position', 'image', 'admin_img', 'pub_date']
    readonly_fields = ['admin_img']
    actions = [duplicate_action]

class ArticleAdmin(admin.ModelAdmin):
    """An admin model wrapper for the Article model"""
    list_display = ['title', 'subtitle', 'pub_date']
    fields = ['title', 'subtitle', 'text', 'image', 'admin_img', 'pub_date']
    readonly_fields = ['admin_img']
    actions = [duplicate_action]

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
