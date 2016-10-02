__author__ = 'Patrick'
from django.conf.urls import url
import exp_services.views as views

urlpatterns = [

    url(r'api/v1/services/daddies', views.get_daddies_from_models)
]