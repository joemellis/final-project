from django.shortcuts import render,redirect
from .models import Home  
from .forms import AdvertForm
import cloudinary.uploader

#def index(request):
#    return render(request,'home/index.html')
def index(request):
    home_list = Home.objects.all()
    return render(request, 'home/index.html', {'home_list': home_list})

# ------------------------------------------------CREATE A POST

def create_advert(request):
    if request.method == 'POST':
        form = AdvertForm(request.POST, request.FILES)
        if form.is_valid():
            # Upload image to Cloudinary
            image = request.FILES['image']
            result = cloudinary.uploader.upload(image)
            # Save image URL to the model
            instance = form.save(commit=False)
            instance.image_url = result['secure_url']
            instance.save()
            # Redirect to the home page (index) on success
            return redirect('index')
    else:
        form = AdvertForm()
    return render(request, 'create_advert.html', {'form': form})

def success_page(request):
    return render(request, '/')
# ------------------------------------------------SEARCH FUNCTION STILL WORK IN PROGRESS
def search_results(request):
    # Get form inputs
    search_query = request.GET.get('search')
    section = request.GET.get('section')
    location = request.GET.get('location')
    # Get filtered homes based on form inputs
    filtered_homes = Home.objects.all()
    if search_query:
        filtered_homes = filtered_homes.filter(title__icontains=search_query)
    # Apply other filters as needed
    # Render template with filtered results
    return render(request, 'home/search_results.html', {'filtered_homes': filtered_homes})