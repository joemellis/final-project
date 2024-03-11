from django.shortcuts import render
from .models import Home  

#def index(request):
#    return render(request,'home/index.html')
    
def index(request):
    home_list = Home.objects.all()  # Replace with your actual queryset
    return render(request, 'home/index.html', {'home_list': home_list})

def index(request):
    dummy_data = [
        {'title': 'Dummy Item 1', 'price': 100.0, 'image': '/path/to/image1.jpg'},
        {'title': 'Dummy Item 2', 'price': 200.0, 'image': '/path/to/image2.jpg'},
        # Add more dummy data as needed
    ]
    return render(request, 'home/index.html', {'home_list': dummy_data})
