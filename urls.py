from django.conf.urls import url
from clubm8web import views

app_name = 'clubm8web'

urlpatterns = [
    url(r'^$',
        views.IndexView.as_view(),
        name='index'),
]
