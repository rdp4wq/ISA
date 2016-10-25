from django.conf.urls import url
import exp_services.views as views

urlpatterns = [
    url(r'^api/v1/services/users/$', views.get_users_from_models),
    url(r'^api/v1/services/users/(?P<pk>[0-9]+)/$', views.get_user_from_models),
    url(r'^api/v1/services/babies/$', views.get_babies_from_models, name='baby_all'),
    url(r'^api/v1/services/babies/(?P<pk>[0-9]+)/$', views.get_baby_from_models, name='baby_detail'),
    url(r'^api/v1/services/daddies/$', views.get_daddies_from_models, name='daddies_all'),
    url(r'^api/v1/services/daddies/(?P<pk>[0-9]+)/$', views.get_daddy_from_models, name='daddy_detail'),
    url(r'^api/v1/login/$', views.login, name='login'),
    url(r'^api/v1/authenticate/$', views.authenticate, name='authenticate'),
    url(r'api/v1/dates/new$', views.create_date, name='date_new'),
    url(r'api/v1/dates/', views.get_dates, name='dates'),
    url(r'api/v1/register/', views.create_user, name='user_new'),

]
