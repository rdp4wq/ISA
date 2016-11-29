from django.conf.urls import url
import webapp.views as views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^daddies/$', views.daddies),
    # url(r'^babies/$', views.babies),
    # url(r'^babies/(?P<baby_id>[0-9]+)/$', views.baby_detail),
    url(r'^dates/$', views.dates),
    url(r'search', views.search),
    url(r'login', views.login),
    url(r'logout', views.logout),
    url(r'register', views.register),
    url(r'create', views.create_date),
    url(r'check', views.check_if_user_exists)
]
