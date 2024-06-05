from django.shortcuts import render
from .forms import ApartmentListingForm

def index(request):
    return render(request, 'index.html')

def form_view(request):
    if request.method == 'POST':
        form = ApartmentListingForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to success page or display a success message
    else:
        form = ApartmentListingForm()

    return render(request, 'form.html', {'form': form})
