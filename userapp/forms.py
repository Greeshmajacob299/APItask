from django import forms

from userapp.models import Destination


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'

        widgets = {
            'placename': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the place name'}),
            'weather': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the weather'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the district'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the state'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the description'}),

        }

