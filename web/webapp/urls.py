__author__ = 'Patrick'
from django.conf.urls import url
import webapp.views as views

urlpatterns = [

    url(r'^$', views.index),
    url(r'api/v1/daddies', views.daddies)
]