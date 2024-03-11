from django.shortcuts import render
from .models import Home  

#def index(request):
#    return render(request,'home/index.html')
def index(request):
    home_list = Home.objects.all()
    return render(request, 'home/index.html', {'home_list': home_list})
