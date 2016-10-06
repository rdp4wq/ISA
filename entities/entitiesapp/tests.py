from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from entitiesapp.models import Baby, Daddy

class EntitiesTestCase(TestCase):
    def setUp(self):
        Daddy.objects.create(id=1, first_name='sugar', last_name='daddy', income='100', city='Fairfax', state='VA')
        Baby.objects.create(id=1, first_name='sugar', last_name='daddy', city='Fairfax', state='VA')


    def test_daddy(self):
        response = self.client.get(reverse('get_daddies_list')+"1/")
        self.assertContains(response, 'id')

    def test_daddies_list(self):
        print(reverse('get_daddies_list'))
        response = self.client.get(reverse('get_daddies_list'))

        self.assertContains(response, 'daddies')

    def test_daddies_income(self):
        response = self.client.get(reverse('get_daddies_list')+"1/")
        self.assertContains(response, 'income')

    def test_daddies_state(self):
        response = self.client.get(reverse('get_daddies_list')+"1/")
        self.assertContains(response, 'state')

    def test_daddies_city(self):
        response = self.client.get(reverse('get_daddies_list')+"1/")
        self.assertContains(response, 'city')

    def test_babies(self):
        response = self.client.get(reverse('get_babies_list'))
        self.assertContains(response, 'babies')

    def test_babies_name(self):
        response = self.client.get(reverse('get_babies_list')+"1/")
        self.assertContains(response, 'first_name')

    def tearDown(self):
        pass