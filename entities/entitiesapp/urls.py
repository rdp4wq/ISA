from django.conf.urls import url, include
import entitiesapp.views as views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users/username', views.UserByUsernameViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'authenticators/user', views.AuthenticatorByUserViewSet)
router.register(r'authenticators', views.AuthenticatorViewSet)
router.register(r'dates', views.DateViewSet, 'dates')


urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]
