
from django.shortcuts import render
from .forms import Apartment

def index(request):
    return render(request, 'index.html')

def form_view(request):
    return render(request, 'form.html')


def form_view(request):
    if request.method == 'POST':
        form = Apartment(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Apartment()

    # Debugging: print form to console
    print(form)

    return render(request, 'form.html', {'form': form})
