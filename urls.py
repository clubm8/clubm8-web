from django.conf.urls import url
from clubm8web import views

app_name = 'clubm8web'

urlpatterns = [
    url(r'^$',
        views.IndexView.as_view(),
        name='index'),
    url(r'^news/$',
        views.NewsView.as_view(),
        name='news'),
    url(r'^events/$',
        views.IndexView.as_view(),
        name='index'),
    url(r'^specials/$',
        views.SpecialsView.as_view(),
        name='specials'),
]
