from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView

from analytics.models import TagView
from .models import Tag

class TagDetailView(DetailView):
    model = Tag

    def get_context_data(self, *args, **kwargs):
            context = super(TagDetailView, self).get_context_data(*args, **kwargs)
            if self.request.user.is_authenticated:
                tags = self.get_object()
                new_view = TagView.objects.add_count(self.request.user, tags)
            return context

class TagListView(ListView):
    model = Tag

    def get_queryset(self):
        return Tag.objects.all()
