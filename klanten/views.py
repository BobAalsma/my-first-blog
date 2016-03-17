""" 
klant: views.py   

klanten gaat over opdrachtgevers / klantorganisaties

"""

from django.shortcuts import render
from django.utils import timezone
from .models import Klant


def klant_lijst(request):
#    klanten = Klant.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    klanten = Klant.objects.all()
    return render(request, 'klanten/klant_lijst.html', {'klanten': klanten})
