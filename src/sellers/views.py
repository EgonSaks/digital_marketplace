from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormMixin

# Create your views here.
from billing.models import Transaction
from products.models import Product
from digitalmarket.mixins import LoginRequiredMixin
from .models import SellerAccount

from .forms import NewSellerForm

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
            context["transactions"] = Transaction.objects.filter(product__in=products)
        else:
            passs

        return render(request, "sellers/dashboard.html", context)

    def form_valid(self, form):
        valid_data = super(SellerDashboard, self).form_valid(form)
        obj = SellerAccount.objects.create(user=self.request.user)
        return valid_data
