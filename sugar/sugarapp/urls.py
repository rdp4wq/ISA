from django.conf.urls import url
import sugarapp.views as views

urlpatterns = [
    url(r'^api/babies/(?P<pk>[0-9]+)/$', views.BabyDetail.as_view()),
    url(r'^api/babies/$', views.BabyList.as_view()),
    url(r'^api/daddies/(?P<pk>[0-9]+)/$', views.DaddyDetail.as_view()),
    url(r'^api/daddies/$', views.DaddyList.as_view()),
    url(r'^$', views.index)
]