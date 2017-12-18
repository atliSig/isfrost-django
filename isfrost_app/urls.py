"""URL configuration for for the isfrost_app app"""
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
	   path('', views.index_view, name='index'),
	   path('products/categories/', views.product_category_list_view.as_view(),
	   		   name='product_categories'),
	   path('products/categories/<int:pk>/', views.product_category_detail_view.as_view(),
	   		   name='product_category'),
	   path('products/items/<int:pk>/', views.product_detail_view.as_view(), name='product'),
	   path('services/categories/', views.service_category_list_view.as_view(),
	   		   name='service_categories'),
	   path('services/categories/<int:pk>/', views.service_category_detail_view.as_view(),
	   		   name='service_category'),
	   path('services/items/<int:pk>/', views.service_detail_view.as_view(), name='service'),
	   path('staff/', views.staff_list_view.as_view(), name='staff_list'),
	   path('staff/<int:pk>/', views.staff_detail_view.as_view(), name='staff'),
	   path('articles/<int:pk>/', views.article_detail_view.as_view(), name='article'),
	   path('articles/', views.article_list_view.as_view(), name='articles'),
]