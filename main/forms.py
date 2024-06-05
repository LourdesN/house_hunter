from django import forms
from .models import Apartment

class ApartmentListingForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['title', 'description', 'price', 'location', 'image', 'is_for_sale', 'is_for_rent']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'price': 'Price (shs)',
            'location': 'Location',
            'image': 'Image',
            'is_for_sale': 'For Sale',
            'is_for_rent': 'For Rent',
        }