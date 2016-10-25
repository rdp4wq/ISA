from django.test import TestCase
from django.core.urlresolvers import reverse
from django.http import Http404

# Create your tests here.
class ServicesTestCase(TestCase):
    def test_valid_login(self):
        response = self.client.post(reverse('login'), {'username': 'Ry', 'password': 'password'})
        self.assertContains(response, 'authenticator')

    def test_invalid_login(self):
        response = self.client.post(reverse('login'), {'username': 'Ry', 'password': 'not_the_right_password'})
        self.assertEqual(response.status_code, 404)
