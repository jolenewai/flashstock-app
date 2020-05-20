from django import forms
from .models import Photographer


class PhotographerForm(forms.ModelForm):
    class Meta:
        model = Photographer
        fields = (
            'display_name',
            'dob',
            'profile_img',
            'address_line1',
            'address_line2',
            'postal_code',
            'city',
            'country',
            'country_code',
            'contact_number'
        )