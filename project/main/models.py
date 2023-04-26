from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class PlaceMemory(models.Model):
    """Place memory model"""

    place = models.CharField(
        max_length=300,
        verbose_name=_('City'),
    )
    memory = models.TextField(
        verbose_name=_('Description'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at'),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated_at'),
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='memories',
        related_query_name='memory',
        verbose_name=_('User'),
    )

    class Meta:
        verbose_name = _('Memory of a place')
        verbose_name_plural = _('Memories of places')
