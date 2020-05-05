from django.shortcuts import render
from django.http import Http404

# Create your views here.
from .models import Product

def detail_view(request, object_id=None):
    if object_id is not None:
        product = Product.objects.get(id=object_id)
        template = "detail_view.html"
        context = {
                    "object" : product
                }
    else:
        raise Http404

    return render(request, template, context)

def list_view(request):
    # list of items
    queryset = Product.objects.all()
    template = "list_view.html"
    context = {
        "queryset" : queryset
    }
    return render(request, template, context)
