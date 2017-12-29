"""The model configuration for the isfrost_app app"""
import datetime
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

class ProductCategory(models.Model):
    """The ProductCategory model class"""
    name = models.CharField('Nafn vöruflokks', max_length=200)
    pub_date = models.DateTimeField('Búið til þann', default=timezone.now)
    image = models.ImageField(upload_to='images/product_categories/%Y/%m', default='images/defaults/product.png', blank=True, null=True)
    short_description = models.TextField('Stutt lýsing um vöruflokk', default='Engar nánari upplýsingar')
    detailed_description = models.TextField('Nánar um vöruflokk', default='Engar nánari upplýsingar', null=True)
    def admin_img(self):
        """Returns a markup block to display image in admin view"""
        return mark_safe('<img src="%s"/>' % self.image.url)
    admin_img.allow_tags = True
    admin_img.short_description = 'Valin mynd'
    class Meta:
        verbose_name = 'Vöruflokkur'
        verbose_name_plural = 'Vöruflokkar'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    """The Product model class"""
    name = models.CharField('Product name', max_length=200)
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, default=1)
    detailed_description = models.TextField('Nánari upplýsingar um vöru', default='Engar nánari upplýsingar', null=True)
    short_description = models.TextField('Stutt lýsing um vöru', default='Engar nánari upplýsingar', null=True)
    price = models.IntegerField('Verð', blank=True, null=True)
    image = models.ImageField(upload_to='images/products/%Y/%m', default='images/defaults/product.png', blank=True, null=True)
    def admin_img(self):
        """Returns a markup block to display image in admin view"""
        return mark_safe('<img src="%s"/>' % self.image.url)
    admin_img.allow_tags = True
    admin_img.short_description = 'Valin mynd'
    def is_new(self):
        """Returns true if object was created in the last 30 days"""
        now = timezone.now()
        return  now - datetime.timedelta(days=30) <= self.pub_date <= now
    class Meta:
        verbose_name = 'Vara'
        verbose_name_plural = 'Vörur'
        ordering = ['-pub_date']
    
    def __str__(self):
        return self.name


class ServiceCategory(models.Model):
    """The Service category model class"""
    name = models.CharField('Service category name', max_length=200)
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    short_description = models.TextField('Stutt lýsing um þjónustuflokk', default='Engar nánari upplýsingar')
    detailed_description = models.TextField('Nánar um þjónustuflokk', default='Engar nánari upplýsingar', null=True)
    icon = models.CharField('tákn', max_length=20, default='snowflake-o', blank=True, null=True,
        help_text="1. Finna tákn hér: http://fontawesome.io/icons/ "+
        "2. Láta inn nafn, t.d. \"address-book\"")
    def admin_icon(self):
        """Returns a markup block to display icon in admin view"""
        return mark_safe('<span><i class="fa fa-%s"></i></span>' % self.icon)
    admin_icon.allow_tags = True
    admin_icon.short_description = 'Valið tákn'
    class Meta:
        verbose_name = 'Þjónustuflokkur'
        verbose_name_plural = 'Þjónustuflokkar'

    def __str__(self):
        return self.name

class Service(models.Model):
    """The Service model class"""
    name = models.CharField('Þjónusta', max_length=200)
    pub_date = models.DateTimeField('Búið til þann', default=timezone.now)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, default=1)
    description = models.TextField('Um þjónustu', default='Engar nánari upplýsingar', blank=True)
    class Meta:
        verbose_name = 'Þjónusta'
        verbose_name_plural = 'Þjónustur'

    def __str__(self):
        return self.name

class Staff(models.Model):
    """The staff model class"""
    name = models.CharField('nafn', max_length=200)
    pub_date = models.DateTimeField('Búið til þann', default=timezone.now)
    position = models.CharField('Deild eða starfsheiti', max_length=200, default='Almennur starfsmaður')
    email = models.EmailField('Póstur', max_length=200, blank=True)
    phone = models.CharField('Símanúmer', max_length=7, blank=True)
    image = models.ImageField(upload_to='images/staff/%Y/%m', default='images/defaults/user.png', blank=True, null=True)
    def admin_img(self):
        """Returns a markup block to display image in admin view"""
        return mark_safe('<img src="%s"/>' % self.image.url)
    admin_img.allow_tags = True
    admin_img.short_description = 'Valin mynd'
    class Meta:
        verbose_name = 'Starfsmaður'
        verbose_name_plural = 'Starfsmenn'
        ordering = ['name']
    
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
    image = models.ImageField(upload_to='images/articles/%Y/%m', default='images/defaults/article.png', blank=True, null=True)
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
    introduction = models.TextField('Lýsing á forsíðu', blank=True)
    service_description = models.TextField('Lýsing fyrir þjónustu', blank=True)
    product_description = models.TextField('Lýsing fyrir vörur', blank=True)
    about_description = models.TextField('Lýsing fyrir fyrirtækjaupplýsingar', blank=True)
    news_description = models.TextField('Lýsing á fréttum', blank=True)
    cover_image = models.ImageField('Forsíðumynd', upload_to='images/company/%Y/%m', null=True)   
    def admin_img(self):
        """Returns a markup block to display image in admin view"""
        return mark_safe('<img src="%s" style="max-width:300px"/>' % self.cover_image.url)
    admin_img.allow_tags = True
    admin_img.short_description = 'Forsíðumynd'
    class Meta:
        verbose_name =  'Forsíða'
        verbose_name_plural = 'Forsíðan'

class AboutPage(models.Model):
    """The about page model class"""
    text = models.TextField('Texti á síðu um ísfrost', blank=True)

    class Meta:
        verbose_name = 'Um Ísfrost'
        verbose_name_plural = 'Um Ísfrost'