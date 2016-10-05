from django.conf.urls import url
import webapp.views as views

urlpatterns = [

    url(r'^$', views.index),
    url(r'daddies', views.daddies),
    url(r'babies', views.babies),
    url(r'search', views.search)

]