from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(default='slug-field')    # unique=True
    description = models.TextField(max_length=200, null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99, null=True)
    sales_price = models.DecimalField(max_digits=100,decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural ='Products'
