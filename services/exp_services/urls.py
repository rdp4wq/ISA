from django.conf.urls import url
import exp_services.views as views
from elasticsearch import Elasticsearch
from kafka import KafkaProducer
from services.settings import ENTITIES_URL
import requests
import json

urlpatterns = [
    url(r'^api/v1/services/users/$', views.get_users_from_models),
    url(r'^api/v1/services/users/(?P<pk>[0-9]+)/$', views.get_user_from_models),
    url(r'^api/v1/services/babies/$', views.get_babies_from_models, name='baby_all'),
    url(r'^api/v1/services/babies/(?P<pk>[0-9]+)/$', views.get_baby_from_models, name='baby_detail'),
    url(r'^api/v1/services/daddies/$', views.get_daddies_from_models, name='daddies_all'),
    url(r'^api/v1/services/daddies/(?P<pk>[0-9]+)/$', views.get_daddy_from_models, name='daddy_detail'),
    url(r'^api/v1/login/$', views.login, name='login'),
    url(r'^api/v1/authenticate/$', views.authenticate, name='authenticate'),
    url(r'^api/v1/dates/new/$', views.create_date, name='date_new'),
    url(r'^api/v1/dates/$', views.get_dates, name='dates'),
    url(r'^api/v1/register/$', views.create_user, name='user_new'),
    url(r'^api/v1/search/$', views.search, name='search'),
    url(r'^api/v1/startup/$', views.index_dates_at_startup, name='startup')

]

kp = KafkaProducer(bootstrap_servers='kafka:9092')

url = ENTITIES_URL + 'api/v1/dates/'
r = requests.get(url)
body_data = json.loads(r.content.decode('utf8'))
for date in body_data['result']:
    kp.send('new-listings-topic', json.dumps(date).encode('utf-8'))