from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView

# Create your views here.
from billing.models import Transaction
from products.models import Product
from digitalmarket.mixins import LoginRequiredMixin
from .models import SellerAccount

from .forms import NewSellerForm


class SellerTransactionListView(ListView):
    model = Transaction
    template_name ="sellers/transaction_list_view.html"

    def get_queryset(self):
        account = SellerAccount.objects.filter(user=self.request.user)
        if account.exists():
            #products = Product.objects.filter(seller=account)
            #products = Product.objects.filter(seller__in=account)
            #return Transaction.objects.filter(product__in=products)
            return Transaction.objects.filter(product__seller__user=self.request.user)
        return []


class SellerDashboard(LoginRequiredMixin, FormMixin, View):
    form_class = NewSellerForm
    success_url = "/seller/"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get(self, request, *args, **kwargs):
        apply_form = self.get_form() #NewSellerForm()
        account = SellerAccount.objects.filter(user=self.request.user)
        exists = account.exists()
        active = None

        if exists:
            account = account.first()
            active = account.active

        context = {}

        #if the account doesn´t exists, show form
        #if exists and not active, show pending
        #if exists and active show dashboard data

        if not exists and not active:
            context["title"] = "Apply for Account"
            context["apply_form"] = apply_form
        elif exists and not active:
            context["title"] = "Account Pending"
        elif exists and active:
            context["title"] = "Seller Dashboard"
            products = Product.objects.filter(seller=account)
            context["products"] = products
            context["transactions"] = Transaction.objects.filter(product__in=products)[:6]
        else:
            passs

        return render(request, "sellers/dashboard.html", context)

    def form_valid(self, form):
        valid_data = super(SellerDashboard, self).form_valid(form)
        obj = SellerAccount.objects.create(user=self.request.user)
        return valid_data
