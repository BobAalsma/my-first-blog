""" 
klant: admin.py   

klanten gaat over opdrachtgevers / klantorganisaties

"""

from django.contrib import admin
from .models import Klant

admin.site.register(Klant)