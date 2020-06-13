from django.conf import settings
from django.db import models

# Create your models here.

class SellerAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    managers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='manager_sellers', blank=True)
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        verbose_name = 'Seller Account'
        verbose_name_plural = 'Sellers Accounts'
