from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Service, Product

class product_view(generic.DetailView):
	model = Product
	template_name = 'isfrost_app/product.html' 

class service_view(generic.DetailView):
	model = Service
	template_name = 'isfrost_app/service.html'

def index_view(request):
	context = {
		'product_categories' : request.product_categories,
		'service_categories' : request.service_categories
	}
	return render(request, 'isfrost_app/index.html',context)