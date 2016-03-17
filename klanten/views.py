""" 
klant: views.py   

klanten gaat over opdrachtgevers / klantorganisaties

"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from .forms import KlantForm
from .models import Klant

def klant_lijst(request):
    klanten = Klant.objects.order_by('naam')
    return render(request, 'klanten/klant_lijst.html', {'klanten': klanten})

def klant_detail(request, pk):
    klant = get_object_or_404(Klant, pk=pk)
    return render(request, 'klanten/klant_detail.html', {'klant': klant})
    
@login_required
def klant_new(request):
    if request.method == "POST":
            form = KlantForm(request.POST)
            if form.is_valid():
                klant = form.save(commit=False)
                klant.author = request.user
                klant.save()
                return redirect('klant_detail', pk=klant.pk)
    else:
        form = KlantForm()
    return render(request, 'klanten/klant_edit.html', {'form': form})

@login_required
def klant_edit(request, pk):
    klant = get_object_or_404(Klant, pk=pk)
    if request.method == "POST":
        form = KlantForm(request.POST, instance=klant)
        if form.is_valid():
            klant = form.save(commit=False)
            klant.author = request.user
            klant.published_date = timezone.now()
            klant.save()
            return redirect('klant_detail', pk=klant.pk)
    else:
        form = KlantForm(instance=klant)
    return render(request, 'klanten/klant_edit.html', {'form': form})
    
#@login_required
#def klant_draft_list(request):
#    klanten = Klant.objects.filter(published_date__isnull=True).order_by('created_date')
#    return render(request, 'klanten/klant_draft_list.html', {'klanten': klanten})

#@login_required
#def klant_publish(request, pk):
#    klant = get_object_or_404(Klant, pk=pk)
#    klant.publish()
#    return redirect('klanten.views.klant_detail', pk=pk)

@login_required
def klant_remove(request, pk):
    klant = get_object_or_404(Klant, pk=pk)
    klant.delete()
    return redirect('klanten.views.klant_lijst')