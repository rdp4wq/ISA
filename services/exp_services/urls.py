from django.conf.urls import url
import exp_services.views as views

urlpatterns = [
    url(r'^api/v1/services/users/$', views.get_users_from_models),
    url(r'^api/v1/services/users/(?P<pk>[0-9]+)/$', views.get_user_from_models),
    url(r'^api/v1/services/babies/$', views.get_babies_from_models),
    url(r'^api/v1/services/babies/(?P<pk>[0-9]+)/$', views.get_baby_from_models),
    url(r'^api/v1/services/daddies/$', views.get_daddies_from_models),
    url(r'^api/v1/login/$', views.login),
    url(r'^api/v1/authenticate/$', views.authenticate),
    url(r'api/v1/dates/new$', views.create_date),
    url(r'api/v1/dates/', views.get_dates),
    url(r'api/v1/register/', views.create_user),

]
