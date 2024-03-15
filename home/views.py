from django.shortcuts import render
from .models import Home  

#def index(request):
#    return render(request,'home/index.html')
def index(request):
    home_list = Home.objects.all()
    return render(request, 'home/index.html', {'home_list': home_list})

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