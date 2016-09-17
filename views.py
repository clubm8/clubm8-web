from django.shortcuts import render
from django.views import generic

from clubm8core import models

class IndexView(generic.ListView):
    template_name = 'clubm8web/index.html'

    model = models.Slot
