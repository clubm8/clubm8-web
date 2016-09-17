from django.shortcuts import render
from django.views import generic
from datetime import datetime

from clubm8core import models

class IndexView(generic.ListView):
    template_name = 'clubm8web/index.html'

    # TODO maybe only slots in the future?
    model = models.Slot

class NewsView(generic.ListView):
    template_name = 'clubm8web/news.html'

    model = models.News

class SpecialsView(generic.ListView):
    template_name = 'clubm8web/specials.html'

    queryset = models.SpecialOccurrence.objects.filter(date__gt=datetime.now().date())
