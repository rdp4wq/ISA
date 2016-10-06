from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from entitiesapp.models import Baby, Daddy

class EntitiesTestCase(TestCase):
    def setUp(self):
        pass

    def test_daddy(self):
        response = self.client.get(reverse('get_daddy', kwargs={'user_id':1}))
        self.assertContains(response, 'id')

    def test_daddies_list(self):
        response = self.client.get(reverse('get_daddies_list'))
        self.assertContains(response, 'daddies')

    def test_daddies_fields(self):
        response = self.client.get(reverse('get_daddies_list'))

    def tearDown(self):
        pass