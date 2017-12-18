"""Definition of views for the isfrost_app app"""
import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Service, Product, ProductCategory, ServiceCategory, Staff, Article, IndexPage

class product_category_list_view(generic.ListView):
    """A generic list view for product categories"""
    model = ProductCategory

    def get_context_data(self, **kwargs):
        """Gets context for view"""
        context = super().get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

class product_category_detail_view(generic.DetailView):
    """A generic detail view for product categories"""
    model = ProductCategory

    def get_context_data(self, **kwargs):
        """Gets context for view"""
        context = super().get_context_data(**kwargs)
        #context['products'] = Product.object.get('product_category'=self.pk)
        return context

class product_detail_view(generic.DetailView):
    """A generic detail view for products """
    model = Product

    def get_context_data(self, **kwargs):
        """Gets context for view"""
        context = super().get_context_data(**kwargs)
        return context

class service_category_list_view(generic.ListView):
    """A generic list view for service categories"""
    model = ServiceCategory

    def get_context_data(self, **kwargs):
        """Gets context for view"""
        context = super().get_context_data(**kwargs)
        return context

class service_category_detail_view(generic.DetailView):
    """A generic detail view for service categories"""
    model = ServiceCategory

    def get_context_data(self, **kwargs):
        """Gets context for view"""
        context = super().get_context_data(**kwargs)
        return context

class service_detail_view(generic.DetailView):
    """A generic detail view for services"""
    model = Service

    def get_context_data(self, **kwargs):
        """Gets context for view"""
        context = super().get_context_data(**kwargs)
        return context


class staff_list_view(generic.ListView):
    """A generic list view for staff"""
    model = Staff
    
    def get_context_data(self, **kwargs):
        """Gets context for view"""
        context = super().get_context_data(**kwargs)
        return context

class staff_detail_view(generic.DetailView):
    """A generic detail view for staff"""
    model = Staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class article_list_view(generic.ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class article_detail_view(generic.DetailView):
    """A generic detail view for articles"""
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def index_view(request):
    try:
        index = IndexPage.objects.all()[:1].get()
    except:
        index = None
    context = {
        'index' : index,
        'articles': Article.objects.new_items()[:3]
    }
    return render(request, 'isfrost_app/index.html', context)
