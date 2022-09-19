from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import *
from taggit.models import Tag
from django.template.defaultfilters import slugify


class NewsView(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'home.html'


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    news = News.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'news': news,
    }
    return render(request, 'home.html', context)
