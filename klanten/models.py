""" 
klant: models.py   

klanten gaat over opdrachtgevers / klantorganisaties

"""

from django.db import models
from django.utils import timezone


class Klant(models.Model):
    """
    Een Klant betreft de stamgegevens van een opdrachtgever:
    naam organisatie en naam (commerciele) contactpersoon.
    
    Een Klant heeft 0:n ContactPersoon
    
    """
    
    author = models.ForeignKey('auth.User')
    naam = models.CharField('organisatie', max_length=200)
    naam = models.CharField('woomplaats', max_length=200)
    naam = models.CharField('verantwoordelijke', max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = 'klanten'