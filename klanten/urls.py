""" 
klant: urls.py   

klanten gaat over opdrachtgevers / klantorganisaties

"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.klant_lijst, name='klant_lijst'),
]