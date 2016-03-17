""" 
klant: urls.py   

klanten gaat over opdrachtgevers / klantorganisaties

"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.klant_lijst, name='klant_lijst'),
    url(r'^klant/(?P<pk>[0-9]+)/$', views.klant_detail, name='klant_detail'),
    url(r'^klant/new/$', views.klant_new, name='klant_new'),
    url(r'^klant/(?P<pk>[0-9]+)/edit/$', views.klant_edit, name='klant_edit'),
#    url(r'^drafts/$', views.klant_draft_list, name='klant_draft_list'),
#    url(r'^klant/(?P<pk>\d+)/publish/$', views.klant_publish, name='klant_publish'),
    url(r'^klant/(?P<pk>\d+)/remove/$', views.klant_remove, name='klant_remove'),
]