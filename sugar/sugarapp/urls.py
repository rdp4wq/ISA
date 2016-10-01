from django.conf.urls import url
import sugarapp.views as views

urlpatterns = [
    url(r'^api/v1/babies/(?P<pk>[0-9]+)/$', views.BabyDetail.as_view()),
    url(r'^api/v1/babies/$', views.BabyList.as_view()),
    url(r'^api/v1/daddies/(?P<pk>[0-9]+)/$', views.DaddyDetail.as_view()),
    url(r'^api/v1/daddies/$', views.DaddyList.as_view()),
    url(r'^$', views.index)
]