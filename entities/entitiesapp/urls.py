from django.conf.urls import url
import entitiesapp.views as views

urlpatterns = [
    url(r'^api/v1/babies/(?P<pk>[0-9]+)/$', views.BabyDetail.as_view(), name='get_baby'),
    url(r'^api/v1/babies/$', views.BabyList.as_view(), name='get_babies_list'),
    url(r'^api/v1/daddies/(?P<pk>[0-9]+)/$', views.DaddyDetail.as_view(), name='get_daddy'),
    url(r'^api/v1/daddies/$', views.DaddyList.as_view(), name='get_daddies_list'),
    url(r'^$', views.index)
]