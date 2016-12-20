from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

from . import views


app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^blog/(?P<pk>\d+)$', views.DetailView.as_view(), name='post'),
]