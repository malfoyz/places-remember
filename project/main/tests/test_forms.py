from django import forms
from django.contrib.auth.models import User
from django.test import TestCase

from ..forms import PlaceMemoryForm


class PlaceMemoryFormTest(TestCase):
    """Contains unit tests of the PlaceMemoryForm"""

    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create_user(username='ivanov', password='1234567890', email='ivanov@site.ru')

    def test_valid_data(self) -> None:
        form_data = {
            'place': 'Moscow',
            'memory': 'Beatiful!',
            'user': 1,
        }
        form = PlaceMemoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_place_widget(self) -> None:
        form = PlaceMemoryForm()
        attrs_class = form.fields['place'].widget.attrs['class']
        self.assertEquals(attrs_class, 'form-control')

    def test_memory_widget(self) -> None:
        form = PlaceMemoryForm()
        attrs_class = form.fields['memory'].widget.attrs['class']
        self.assertEquals(attrs_class, 'form-control')

    def test_user_widget(self) -> None:
        form = PlaceMemoryForm()
        user_widget = form.fields['user'].widget
        self.assertIsInstance(user_widget, forms.HiddenInput)
