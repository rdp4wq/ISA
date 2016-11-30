from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from entitiesapp.models import User, Date

class EntitiesTestCase(TestCase):
    def setUp(self):
        # Daddy.objects.create(id=1, first_name='sugar', last_name='daddy', income='100', city='Fairfax', state='VA')
        # Baby.objects.create(id=1, first_name='sugar', last_name='daddy', cost='5', city='Fairfax', state='VA')
        # User.objects.create(id=1, first_name='sugar', last_name='baby', email='email@email.com', username='usr', password='pw',
        #                     user_type='Baby', city='town', state='VA', date_created='2016-10-18', date_of_birth='1990-01-01')
        User.objects.create(id=2, first_name='sugar', last_name='daddy', email='email2@email.com', username='usr2', password='pw',
                            user_type='Daddy', city='town', state='VA', date_created='2014-10-18', date_of_birth='1977-01-01', income=100000)
        Date.objects.create(id=1, user= User.objects.create(id=1, first_name='sugar', last_name='baby', email='email@email.com', username='usr', password='pw',
                            user_type='Baby', city='town', state='VA', date_created='2016-10-18', date_of_birth='1990-01-01'), price=500, description="Fun times!")

    #Use Case: able to see a user
    def test_user_id(self):
        response = self.client.get(reverse('users-detail', kwargs={'pk':1}))
        self.assertContains(response, 'id')

    #Use Case: able to see a list of users
    def test_users(self):
        response = self.client.get(reverse('users-list'))
        self.assertContains(response, 'id')

    #Use Case: able to see a user's state
    def test_user_state(self):
        response = self.client.get(reverse('users-detail', kwargs={'pk':1}))
        self.assertContains(response, 'state')

    #Use Case: able to see a user's city
    def test_user_city(self):
        response = self.client.get(reverse('users-detail', kwargs={'pk':1}))
        self.assertContains(response, 'city')

    #Use Case: able to see a user's date of birth
    def test_user_dob(self):
        response = self.client.get(reverse('users-detail', kwargs={'pk':1}))
        self.assertContains(response, 'date_of_birth')

    #Use Case: unable to see a Baby's income
    def test_baby_no_income(self):
        response = self.client.get(reverse('users-detail', kwargs={'pk':1}))
        # jsonresponse = str(response.content, encoding='utf8')
        self.assertContains(response, '\"income\":null')

    #Use Case: able to see a date
    # def test_date_id(self):
    #     response = self.client.get(reverse('dates-detail', kwargs={'pk':1}))
    #     self.assertContains(response, 'id')

    #Use Case: able to see a date's description
    # def test_date_desc(self):
    #     response = self.client.get(reverse('dates-detail', kwargs={'pk':1}))
    #     self.assertContains(response, 'description')

    #Use Case: not able to see a non-existent user
    def test_no_user(self):
        response = self.client.get(reverse('users-detail', kwargs={'pk':3}))
        self.assertEqual(response.status_code, 404)

    #Use Case: not able to see a non-existent date
    def test_no_date(self):
        response = self.client.get(reverse('dates-detail', kwargs={'pk':2}))
        self.assertEqual(response.status_code, 404)

    # #Use Case: able to see a daddy
    # def test_daddy(self):
    #     response = self.client.get(reverse('get_daddies_list')+"1/")
    #     self.assertContains(response, 'id')
    #
    # #Use Case: able to see a daddy
    # def test_no_daddy(self):
    #     response = self.client.get(reverse('get_daddies_list')+"2/")
    #     self.assertEqual(response.status_code, 404)
    #
    # #Use Case: able to see daddy list
    # def test_daddies_list(self):
    #     response = self.client.get(reverse('get_daddies_list'))
    #     self.assertContains(response, 'daddies')
    #
    # #Use Case: able to see daddy income
    # def test_daddies_income(self):
    #     response = self.client.get(reverse('get_daddies_list')+"1/")
    #     self.assertContains(response, 'income')
    #
    # #Use Case: able to see daddy state
    # def test_daddies_state(self):
    #     response = self.client.get(reverse('get_daddies_list')+"1/")
    #     self.assertContains(response, 'state')
    #
    # #Use Case: able to see daddy city
    # def test_daddies_city(self):
    #     response = self.client.get(reverse('get_daddies_list')+"1/")
    #     self.assertContains(response, 'city')
    #
    # #Use Case: able to see baby list
    # def test_babies(self):
    #     response = self.client.get(reverse('get_babies_list'))
    #     self.assertContains(response, 'babies')
    #
    # #Use Case: able to see baby first name
    # def test_babies_name(self):
    #     response = self.client.get(reverse('get_babies_list')+"1/")
    #     self.assertContains(response, 'first_name')

    def tearDown(self):
        pass