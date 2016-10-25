from django.conf.urls import url
import webapp.views as views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^daddies/$', views.daddies),
    url(r'^babies/$', views.babies),
    url(r'^babies/(?P<baby_id>[0-9]+)/$', views.baby_detail),
    url(r'search', views.search),
    url(r'login', views.login_page),
    url(r'logout', views.logout)

]
