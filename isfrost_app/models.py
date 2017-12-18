"""The model configuration for the isfrost_app app"""
import datetime
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

class ProductCategory(models.Model):
    """The ProductCategory model class"""
    category_name = models.CharField('Nafn vöruflokks', max_length=200)
    pub_date = models.DateTimeField('Búið til þann', default=timezone.now)
    category_image = models.ImageField(upload_to='images/product_categories/%Y/%m', null=True)
    category_description = models.TextField('Um vöruflokk', default='Engar nánari upplýsingar')
    def admin_img(self):
        """Returns a markup block to display image in admin view"""
        return mark_safe('<img src="%s"/>' % self.category_image.url)
    admin_img.allow_tags = True
    admin_img.short_description = 'Valin mynd'
    class Meta:
        verbose_name = 'Vöruflokkur'
        verbose_name_plural = 'Vöruflokkar'
    
    def __str__(self):
        return self.category_name


class Product(models.Model):
    """The Product model class"""
    product_name = models.CharField('Product name', max_length=200)
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, default=1)
    product_text = models.TextField('About product', default='Engar nánari upplýsingar')
    product_price = models.IntegerField('Product price', default=0)
    product_image = models.ImageField(upload_to='images/products/%Y/%m', null=True)
    def is_new(self):
        """Returns true if object was created in the last 30 days"""
        now = timezone.now()
        return  now - datetime.timedelta(days=30) <= self.pub_date <= now
    class Meta:
        verbose_name = 'Vara'
        verbose_name_plural = 'Vörur'
    
    def __str__(self):
        return self.product_name


class ServiceCategory(models.Model):
    """The Service category model class"""
    category_name = models.CharField('Service category name', max_length=200)
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    category_description = models.TextField('Um vöruflokk', default='Engar nánari upplýsingar')
    category_icon = models.CharField('tákn', max_length=20, null=True,
        help_text="1. Finna tákn hér: http://fontawesome.io/icons/ "+
        "2. Láta inn nafn, t.d. \"address-book\"")
    def admin_icon(self):
        """Returns a markup block to display icon in admin view"""
        return mark_safe('<span><i class="fa fa-%s"></i></span>' % self.category_icon)
    admin_icon.allow_tags = True
    admin_icon.short_description = 'Valið tákn'
    class Meta:
        verbose_name = 'Þjónustuflokkur'
        verbose_name_plural = 'Þjónustuflokkar'

    def __str__(self):
        return self.category_name

class Service(models.Model):
    """The Service model class"""
    service_name = models.CharField('Service name', max_length=200)
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, default=1)
    service_text = models.TextField('About service', default='Engar nánari upplýsingar')
    class Meta:
        verbose_name = 'Þjónusta'
        verbose_name_plural = 'Þjónustur'

    def __str__(self):
        return self.service_name

class Staff(models.Model):
    """The staff model class"""
    name = models.CharField('nafn', max_length=200)
    pub_date = models.DateTimeField('Búið til þann', default=timezone.now)
    position = models.CharField('staða', max_length=200)
    email = models.EmailField('Póstur', max_length=200)
    phone = models.CharField('Símanúmer', max_length=7)
    image = models.ImageField(upload_to='images/staff/%Y/%m', null=True)
    def admin_img(self):
        """Returns a markup block to display image in admin view"""
        return mark_safe('<img src="%s"/>' % self.image.url)
    admin_img.allow_tags = True
    admin_img.short_description = 'Valin mynd'
    class Meta:
        verbose_name = 'Starfsmaður'
        verbose_name_plural = 'Starfsmenn'
    
    def __str__(self):
        return self.name

class ArticleManager(models.Manager):
    def new_items(self):
        return self.filter(pub_date__gte=timezone.now()-datetime.timedelta(days=30))

class Article(models.Model):
    """The article model class"""
    title = models.CharField('Titill', max_length=200)
    subtitle = models.CharField('Undirtexti', max_length=200)
    pub_date = models.DateTimeField('Búið til þann', default=timezone.now)
    text = models.TextField('Texti')
    image = models.ImageField(upload_to='images/articles/%Y/%m', null=True)
    def admin_img(self):
        """Returns a markup block to display image in admin view"""
        return mark_safe('<img src="%s"/>' % self.image.url)
    admin_img.allow_tags = True
    admin_img.short_description = 'Valin mynd'
    class Meta:
        verbose_name =  'Frétt'
        verbose_name_plural = 'Fréttir'
        ordering = ['-pub_date']
    objects = ArticleManager()

    def __str__(self):
        return self.title

class Company(models.Model):
    """The company model class"""
    name = models.CharField('nafn', max_length=200, default='Ísfrost')
    street = models.CharField('Gata', max_length=200)
    postal_code = models.CharField('Póstnúmer', max_length=3)
    city = models.CharField('Staður', max_length=200)
    phone_number = models.CharField('símanúmer', max_length=8)
    email = models.EmailField('póstur', default='isfrost@isfrost.is')
    loc_x = models.CharField('X staðsetningar', default='362464', max_length=6)
    loc_y = models.CharField('Y staðsetningar', default='405894', max_length=6)
    hours_week = models.CharField('Opnunartími virkra daga', default='08-18 alla virka daga', max_length=200)
    hours_weekends = models.CharField('Opnunartími helga', default='Lokað um helgar', max_length=200)
    class Meta:
        verbose_name =  'Fyrirtæki'
        verbose_name_plural = 'Fyrirtækið'
    
    def __str__(self):
        return self.name

class IndexPage(models.Model):
    """The index page model class"""
    introduction = models.TextField('Lýsing á forsíðu', null=True)
    cover_image = models.ImageField('Forsíðumynd', upload_to='images/company/%Y/%m', null=True)   
    def admin_img(self):
        """Returns a markup block to display image in admin view"""
        return mark_safe('<img src="%s" style="max-width:300px"/>' % self.cover_image.url)
    admin_img.allow_tags = True
    admin_img.short_description = 'Forsíðumynd'
    class Meta:
        verbose_name =  'Forsíða'
        verbose_name_plural = 'Forsíðan'