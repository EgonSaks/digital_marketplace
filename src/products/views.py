from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .forms import ProducModelForm
from .models import Product

def create_view(request):
    #FORM
    form = ProducModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.sales_price = instance.price
        instance.save()
    template = "create_view.html"
    context = {
            "form": form,
        }
    return render(request, template, context)

def update_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    form = ProducModelForm(request.POST or None, instance = product)
    if form.is_valid():
        instance = form.save(commit=False)
        #instance.sales_price = instance.price
        instance.save()
    template = "update_view.html"
    context = {
            "object" : product,
            "form" : form
            }
    return render(request, template, context)

def detail_slug_view(request, slug=None):
    try:
        product = get_object_or_404(Product, slug=slug)
    except Product.MultipleObjectsReturned:
        product = Product.objects.filter(slug=slug).order_by("title").first()
    template = "detail_view.html"
    context = {
            "object" : product
            }
    return render(request, template, context)

def detail_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    template = "detail_view.html"
    context = {
            "object" : product
            }
    return render(request, template, context)

def list_view(request):
    # list of items
    queryset = Product.objects.all()
    template = "list_view.html"
    context = {
        "queryset" : queryset
    }
    return render(request, template, context)
