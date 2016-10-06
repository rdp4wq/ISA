from django.conf.urls import url
import webapp.views as views

urlpatterns = [

    url(r'^$', views.index),
    url(r'daddies', views.daddies),
    url(r'babies', views.babies),
    url(r'^baby/(?P<baby_id>[0-9]+)/$', views.babyDetail),
    url(r'search', views.search)

]