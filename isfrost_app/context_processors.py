"""Custom context processors for the isfrost_app app"""
from .models import Company, ProductCategory, ServiceCategory
def company(request):
	try:
		return {'company': Company.objects.all()[:1].get()}
	except:
		return {'company': None} 

def nav(request):
	return {
		'product_categories': ProductCategory.objects.all(),
		'service_categories': ServiceCategory.objects.all()
	}
