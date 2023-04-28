from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.test import RequestFactory, TestCase
from django.urls import reverse

from ..models import PlaceMemory
from ..views import index


class IndexViewTest(TestCase):
    """Contains unit tests of the index view"""

    @classmethod
    def setUpTestData(cls) -> None:
        user = User.objects.create_user(username='ivanov', password='1234567890', email='ivanov@site.ru')
        number_of_memories = 20
        for num in range(number_of_memories):
            PlaceMemory.objects.create(place=f'Place {num}', memory=f'Memory {num}', user=user)

    def test_view_url_exists_at_desired_location(self) -> None:
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')