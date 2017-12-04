from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
	path('', views.index_view, name='index'),
	path('products/<int:pk>/', views.product_view.as_view(), name='product'),
	path('services/<int:pk>/', views.service_view.as_view(), name='service')
]