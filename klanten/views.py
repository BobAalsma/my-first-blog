""" 
klant: views.py   

klanten gaat over opdrachtgevers / klantorganisaties

"""

from django.shortcuts import render

def klant_lijst(request):
    return render(request, 'klanten/klant_lijst.html')
