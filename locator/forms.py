from django import forms
from .models import parent_loc, Location

class ParentLocationForm(forms.ModelForm):
    class Meta:
        model = parent_loc
        fields = ['name']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['parent', 'name', 'status']
