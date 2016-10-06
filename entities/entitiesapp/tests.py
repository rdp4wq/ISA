from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from entitiesapp.models import Baby, Daddy

class EntitiesTestCase(TestCase):
    def setUp(self):
        Daddy.objects.create(id=1, first_name='sugar', last_name='daddy', income='100', city='Fairfax', state='VA')
        Baby.objects.create(id=1, first_name='sugar', last_name='daddy', cost='5', city='Fairfax', state='VA')

    #Use Case: able to see a daddy
    def test_daddy(self):
        response = self.client.get(reverse('get_daddies_list')+"1/")
        self.assertContains(response, 'id')

    #Use Case: able to see a daddy
    def test_no_daddy(self):
        response = self.client.get(reverse('get_daddies_list')+"2/")
        self.assertEqual(response.status_code, 404)

    #Use Case: able to see daddy list
    def test_daddies_list(self):
        response = self.client.get(reverse('get_daddies_list'))
        self.assertContains(response, 'daddies')

    #Use Case: able to see daddy income
    def test_daddies_income(self):
        response = self.client.get(reverse('get_daddies_list')+"1/")
        self.assertContains(response, 'income')

    #Use Case: able to see daddy state
    def test_daddies_state(self):
        response = self.client.get(reverse('get_daddies_list')+"1/")
        self.assertContains(response, 'state')

    #Use Case: able to see daddy city
    def test_daddies_city(self):
        response = self.client.get(reverse('get_daddies_list')+"1/")
        self.assertContains(response, 'city')

    #Use Case: able to see baby list
    def test_babies(self):
        response = self.client.get(reverse('get_babies_list'))
        self.assertContains(response, 'babies')

    #Use Case: able to see baby first name
    def test_babies_name(self):
        response = self.client.get(reverse('get_babies_list')+"1/")
        self.assertContains(response, 'first_name')

    def tearDown(self):
        pass