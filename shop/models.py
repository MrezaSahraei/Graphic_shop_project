from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    CATEGORY_CHOICES_BY_TYPE=(
    ('Mining', 'mine'),
    ('Gaming', 'game'),
    ('Computing', 'cump'),
    ('Design', 'dsgn')

    )
    CATEGORY_CHOICES_BY_PRICE= (
    ('Economical-Level', 'Economical-Level' ),
    ('Mid-Range', 'Mid-Range' ),
    ('High-End', 'High-End')
    )
    usage_type = models.CharField(max_length=20, choices=CATEGORY_CHOICES_BY_TYPE, default='Gaming')
    slug = models.SlugField(max_length=255, unique=True)


    class Meta:
        ordering = ['usage_type']
        indexes = [
            models.Index(fields=['usage_type'])
        ]

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.usage_type


class Product(models.Model):

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    inventory = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    off = models.PositiveIntegerField(default=0)
    new_price = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    file = models.ImageField(upload_to="product_images/%Y/%m/%d")
    title = models.CharField(max_length=250, verbose_name="عنوان", null=True, blank=True)
    description = models.TextField(verbose_name="توضیحات", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]



class ProductFeature(models.Model):
    MANUFACTURER = (
    ('NVIDIA', 'NVIDIA'),
    ('AMD', 'AMD'),
    ('OTHER', 'OTHER')
    )
    SUGGESTED_RESOLUTION = (
    ('720', '720'),
    ('1080', '1080'),
    ('2k', '2k'),
    ('4k', '4k'),
    ('8k', '8k')
    )
    PCIE_INTERFACES = (
    ('2.0', '2.0'),
    ('3.0', '3.0'),
    ('4.0','4.0'),
    ('5.0', '5.0')
    )

    product = models.ForeignKey(Product, related_name='features', on_delete=models.CASCADE)
    memory = models.PositiveIntegerField(default=0)
    card_length = models.PositiveIntegerField(default=0)
    manufacturer = models.CharField(max_length=20, choices=MANUFACTURER, default='OTHER')
    interface = models.CharField(choices=PCIE_INTERFACES, default='2.0')
    tdp = models.PositiveIntegerField(default=0)
    suggested_resolution = models.CharField(max_length=20, choices=SUGGESTED_RESOLUTION, default='720')


