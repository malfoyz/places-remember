from django import forms

from .models import PlaceMemory


class PlaceMemoryForm(forms.ModelForm):
    """Form associated with the place memory model"""

    class Meta:
        model = PlaceMemory
        fields = '__all__'
        widgets = {
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'memory': forms.Textarea(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(),
        }
