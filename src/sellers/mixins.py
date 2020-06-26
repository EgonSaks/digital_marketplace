import datetime
from billing.models import Transaction
from digitalmarket.mixins import LoginRequiredMixin
from products.models import Product

from .models import SellerAccount

class SellerAccountMixin(LoginRequiredMixin, object):
    account = None
    products = []
    transactions = []

    def get_account(self):
        user = self.request.user
        account = SellerAccount.objects.filter(user=user)
        if account.exists() and account.count() == 1:
            self.account = account.first()
            return account.first()
        return None

    def get_products(self):
        account = self.get_account()
        products = Product.objects.filter(seller=account)
        self.products = products
        return products

    def get_transactions(self):
        products = self.get_products()
        transactions = Transaction.objects.filter(product__in=products)
        return transactions

    def get_transactions_today(self):
        today = datetime.date.today()
        today_min = datetime.datetime.combine(today, datetime.time.min)
        today_max = datetime.datetime.combine(today, datetime.time.max)
        return self.get_transactions().filter(timestamp__range=(today_min, today_max))
