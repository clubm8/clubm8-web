from django.shortcuts import render
from django.views import generic

from clubm8core import models

class IndexView(generic.TemplateView):
    template_name = 'clubm8web/index.html'
