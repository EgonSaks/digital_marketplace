from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Tag

class TagDetailView(DetailView):
    model = Tag

class TagListView(ListView):
    model = Tag

    def get_queryset(self):
        return Tag.objects.all()
