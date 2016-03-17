""" 
klant: views.py   

klanten gaat over opdrachtgevers / klantorganisaties

"""

from django import forms

from .models import Klant

class KlantForm(forms.ModelForm):

    class Meta:
        model = Klant
        fields = (
            'naam', 
            'woonplaats',
            'verantwoordelijke',
        )