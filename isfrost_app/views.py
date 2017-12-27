"""Definition of views for the isfrost_app app"""
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from .models import Service, Product, ProductCategory, ServiceCategory, Staff, Article, IndexPage

class product_category_list_view(generic.ListView):
    """A generic list view for product categories"""
    model = ProductCategory
    paginate_by = 10
    def get_context_data(self, **kwargs):
        """Gets context for view"""
        context = super().get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

class product_category_detail_view(generic.DetailView):
    """A generic list view for product categories"""
    model = ProductCategory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = Product.objects.filter(product_category=context['object'].pk)[:3]
        return context


class product_list_view(generic.ListView):
    """A generic list view for products"""
    model = Product
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def products_by_category(request, pk):
    """A view for products by categories"""
    product_list = Product.objects.filter(product_category=pk)
    paginator = Paginator(product_list, 9)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products': products,
        'category': ProductCategory.objects.get(pk=pk)
    }
    return render(request,'isfrost_app/products_by_category_list.html', context)


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
    paginate_by = 10
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
    paginate_by = 9
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class article_detail_view(generic.DetailView):
    """A generic detail view for articles"""
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = Article.objects.all().exclude(pk=context['object'].pk)[:3]
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
