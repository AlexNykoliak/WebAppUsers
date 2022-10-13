from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from backend.models import User


class PostTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='oleksandr',
            email='oleksandr@email.com',
            password='oleksandr'
        )

        self.user = User.objects.create(
            username='test',
            password='password',
            date_joined='1484526287',
        )

    def test_string_representation(self):
        user = User(username='oleksandr')
        self.assertEqual(str(user), user.username)

    def test_user_content(self):
        self.assertEqual(f'{self.user.username}', 'test')
        self.assertEqual(f'{self.user.date_joined}', '1484526287')
        self.assertEqual(f'{self.user.password}', 'password')

    def test_user_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')
        self.assertTemplateUsed(response, 'home.html')

    def test_user_detail_view(self):
        response = self.client.get('/user/1/')
        no_response = self.client.get('/user/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test')
        self.assertTemplateUsed(response, 'user_detail.html')
