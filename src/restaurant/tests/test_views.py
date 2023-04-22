
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

from django.test import TestCase
from django.urls import reverse

from ..models import Menu

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from ..serializers import MenuItemSerializer

class MenuListViewTest(TestCase):

    #@classmethod
    def setUp(self):

        numberMenus = 2

        self.title = ["Cola", "Tomato"]
        self.price = [4.0, 7.0]
        self.inventory = [5, 4]

        for menu_id in range(numberMenus):
            menu = Menu.objects.create(
                title=self.title[menu_id],
                price=self.price[menu_id],
                inventory=self.inventory[menu_id]
            )
            menu.save()

        self.client = APIClient()

        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            email='admin@example.com',
            password='testpass123',
        )



    def test_getall(self):

        user = User.objects.get(username='admin')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.get('/restaurant/menu/')

        for index, item in enumerate(response.data):

            self.assertEqual(item['title'], self.title[index])
            self.assertEqual(float(item['price']), self.price[index])
            self.assertEqual(item['inventory'], self.inventory[index])