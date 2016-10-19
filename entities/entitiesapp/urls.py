from django.conf.urls import url, include
import entitiesapp.views as views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'authenticators', views.AuthentiactorViewSet)
router.register(r'dates', views.DateViewSet)

urlpatterns = [
    url(r'^api/v1/login/$', views.login, name='login'),
    url(r'^api/v1/', include(router.urls)),
]