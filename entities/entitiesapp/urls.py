from django.conf.urls import url
import entitiesapp.views as views

urlpatterns = [
    url(r'^api/v1/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='get_user'),
    url(r'^api/v1/users/$', views.UserList.as_view(), name='get_users_list'),
    url(r'^api/v1/login/$', views.login, name='login')
]