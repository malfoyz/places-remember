from django.contrib.auth.models import User
from django.db import models
from django.test import TestCase

from ..models import PlaceMemory


class PlaceMemoryModelTest(TestCase):
    """Contains unit tests of the PlaceMemory model"""

    @classmethod
    def setUpTestData(cls) -> None:
        user = User.objects.create_user(username='ivanov', password='1234567890', email='ivanov@site.ru')
        PlaceMemory.objects.create(place='Moscow', memory='Beatiful!', user=user)

    def test_place_label(self) -> None:
        place_memory = PlaceMemory.objects.get(pk=1)
        field_label = place_memory._meta.get_field('place').verbose_name
        self.assertEquals(field_label, 'Place')

    def test_memory_label(self) -> None:
        place_memory = PlaceMemory.objects.get(pk=1)
        field_label = place_memory._meta.get_field('memory').verbose_name
        self.assertEquals(field_label, 'Memory')

    def test_created_at_label(self) -> None:
        place_memory = PlaceMemory.objects.get(pk=1)
        field_label = place_memory._meta.get_field('created_at').verbose_name
        self.assertEquals(field_label, 'Created at')

    def test_updated_at_label(self) -> None:
        place_memory = PlaceMemory.objects.get(pk=1)
        field_label = place_memory._meta.get_field('updated_at').verbose_name
        self.assertEquals(field_label, 'Updated at')

    def test_user_label(self) -> None:
        place_memory = PlaceMemory.objects.get(pk=1)
        field_label = place_memory._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'User')

    def test_model_label(self) -> None:
        place_memory = PlaceMemory.objects.get(pk=1)
        label = place_memory._meta.verbose_name
        self.assertEquals(label, 'Memory of a place')

    def test_model_label_plural(self) -> None:
        place_memory = PlaceMemory.objects.get(pk=1)
        label = place_memory._meta.verbose_name_plural
        self.assertEquals(label, 'Memories of places')

    def test_model_ordering(self) -> None:
        place_memory = PlaceMemory.objects.get(pk=1)
        ordering = place_memory._meta.ordering
        self.assertEquals(ordering, ('-updated_at',))

    def test_place_max_length(self) -> None:
        place_memory = PlaceMemory.objects.get(pk=1)
        max_length = place_memory._meta.get_field('place').max_length
        self.assertEquals(max_length, 300)

    def test_user_on_delete(self) -> None:
        place_memory = PlaceMemory.objects.get(pk=1)
        on_delete = place_memory._meta.get_field('user').remote_field.on_delete
        self.assertEquals(on_delete, models.CASCADE)

    def test_user_related_name(self) -> None:
        place_memory = PlaceMemory.objects.get(pk=1)
        related_name = place_memory._meta.get_field('user').remote_field.related_name
        self.assertEquals(related_name, 'memories')

    def test_user_related_query_name(self) -> None:
        place_memory = PlaceMemory.objects.get(pk=1)
        related_query_name = place_memory._meta.get_field('user').remote_field.related_query_name
        self.assertEquals(related_query_name, 'memory')

    def test_created_at_auto_now_add(self) -> None:
        place_memory = PlaceMemory.objects.get(pk=1)
        auto_now_add = place_memory._meta.get_field('created_at').auto_now_add
        self.assertEquals(auto_now_add, True)

    def test_updated_at_auto_now(self) -> None:
        place_memory = PlaceMemory.objects.get(pk=1)
        auto_now = place_memory._meta.get_field('updated_at').auto_now
        self.assertEquals(auto_now, True)

    def test_object_name_is_place(self) -> None:
        place_memory = PlaceMemory.objects.get(pk=1)
        expected_object_name = place_memory.place
        self.assertEquals(expected_object_name, str(place_memory))