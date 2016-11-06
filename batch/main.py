from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
import time
import json


es = Elasticsearch(['es'])
try:
    kc = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
except:
    time.sleep(30)
    kc = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])

for msg in kc:
    msg_json = json.loads(msg.value.decode('utf-8'))
    es.index(index='listing_index', doc_type='listing', id=msg_json['id'], body=msg_json)
    es.indices.refresh(index='listing_index')
