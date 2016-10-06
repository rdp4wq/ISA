from django.conf.urls import url
import exp_services.views as views

urlpatterns = [

    url(r'api/v1/services/daddies/$', views.get_daddies_from_models),
    url(r'api/v1/services/babies/$', views.get_babies_from_models),
    url(r'api/v1/services/babies/(?P<pk>[0-9]+)/$', views.get_baby_from_models),

]