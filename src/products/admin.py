from django.contrib import admin

# Register your models here.

from .models import Product, MyProducts

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "description", "price", "sales_price"]
    search_fields = ["title", "description"]
    list_filter = ["price"]
    list_editable = ["sales_price"]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

admin.site.register(MyProducts)
