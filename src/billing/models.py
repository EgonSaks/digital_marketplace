from django.conf import settings
from django.db import models

# Create your models here.
from products.models import Product

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=9.99, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    success = models.BooleanField(default=True)
    # transaction_id_payment_system = Braintree / Stripe
    # payment_method
    # last_four

    def __str__(self):
        return str(self.id)
