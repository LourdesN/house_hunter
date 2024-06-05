from django.shortcuts import render, redirect
from .forms import ApartmentListingForm
from django.contrib import messages
from .models import Apartment


def index(request):
    return render(request, 'index.html')

def form_view(request):
    if request.method == 'POST':
        form = ApartmentListingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Apartment listing created successfully!!')
            return redirect('form.html')
    else:
        form = ApartmentListingForm()

    return render(request, 'form.html', {'form': form})

def apartment_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'list.html', {'apartments': apartments})
