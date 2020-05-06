from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(blank=True)    # unique=True
    description = models.TextField(max_length=200, null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99, null=True)
    sales_price = models.DecimalField(max_digits=100,decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural ='Products'

def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(product_pre_save_reciever, sender=Product)