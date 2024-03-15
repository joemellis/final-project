from django.shortcuts import render,redirect
from .models import Home  
from .forms import AdvertForm
import cloudinary.uploader
from django.contrib.auth.decorators import login_required


#def index(request):
#    return render(request,'home/index.html')
def index(request):
    home_list = Home.objects.all().order_by('-created_on')
    return render(request, 'home/index.html', {'home_list': home_list})
# ------------------------------------------------CREATE A POST

@login_required
def create_advert(request):
    if request.method == 'POST':
        form = AdvertForm(request.POST, request.FILES)
        if form.is_valid():
            # Set the user field to the current logged-in user
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('index')
    else:
        form = AdvertForm()
    return render(request, 'create_advert.html', {'form': form})

def success_page(request):
    return render(request, '/')




    #------------------------------------------EDIT DELET


@login_required
def user_posts(request):
    user_adverts = Home.objects.filter(user=request.user)
    return render(request, 'home/user_posts.html', {'user_adverts': user_adverts})

@login_required
def edit_advert(request, advert_id):
    advert = Home.objects.get(pk=advert_id)
    if request.method == 'POST':
        form = AdvertForm(request.POST, request.FILES, instance=advert)
        if form.is_valid():
            form.save()
            return redirect('user_posts')
    else:
        form = AdvertForm(instance=advert)
    return render(request, 'home/edit_advert.html', {'form': form})

@login_required
def delete_advert(request, advert_id):
    advert = Home.objects.get(pk=advert_id)
    if request.method == 'POST':
        advert.delete()
        return redirect('user_posts')
    return render(request, 'home/confirm_delete.html', {'advert': advert})

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