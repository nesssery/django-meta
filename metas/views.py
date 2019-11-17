from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from meta.views import Meta
from .models import MetasModels
from . import models
from django.views.generic.detail import DetailView
from django.contrib.staticfiles.templatetags.staticfiles import static
from meta.views import Meta
from django.contrib.sites.shortcuts import get_current_site


def index(request):
    context = {}
    post = MetasModels.objects.get(pk=1)
    context['post'] = post
    context['meta'] = post.as_meta()
    return render(request, 'pages/index.html', context)


class PropView(DetailView):

    def get_context_data(self, **kwargs):
        context = super(PropView, self).get_context_data(self, **kwargs)
        context['meta'] = self.get_object().as_meta(self.request)
        return context


def opengraph(request):
    return render(request, 'pages/opengraph.html')


def sekizai(request):
    return render(request, 'pages/sekizai.html')
