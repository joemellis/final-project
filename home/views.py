from django.shortcuts import render,redirect
from .models import Home  
from .forms import AdvertForm
from.forms import Message
import cloudinary.uploader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import MessageForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from .models import Message
from django.http import HttpResponseNotFound, HttpResponseServerError
from .models import Message

#def index(request):
#    return render(request,'home/index.html')
def index(request):
    home_list = Home.objects.all().order_by('-created_on')
    return render(request, 'home/index.html', {'home_list': home_list})
    paginator = Paginator(home_list, 12)  # Show 12 adverts per page
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    return render(request, 'home/index.html', {'page_obj': page_obj})


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
    if request.method == 'POST':
        # Extract filter parameters from the request body
        search_input = request.POST.get('searchInput')
        section = request.POST.get('section')
        location = request.POST.get('location')
        price_from = request.POST.get('priceFrom')
        price_to = request.POST.get('priceTo')
        for_sale = request.POST.get('forSale')

        # Perform filtering based on the received parameters
        # Query your database and return filtered results
        # Example: filtered_results = YourModel.objects.filter(...)

        # Serialize the filtered results into JSON format
        # Example: serialized_results = [{'field1': 'value1', 'field2': 'value2'}, ...]

        # Return the filtered results as JSON response
        return JsonResponse({'results': serialized_results})

    else:
        # Handle GET requests or other HTTP methods
        return JsonResponse({'error': 'Method not allowed'}, status=405)
def your_view(request):
    categories = Home.objects.values_list('category', flat=True).distinct()
    locations = Home.objects.values_list('location', flat=True).distinct()
    return render(request, 'index.html', {'categories': categories, 'locations': locations})
# ------------------------------------------------Message FUNCTION STILL WORK IN PROGRESS
from django.shortcuts import render, get_object_or_404
from .models import Home, Message

def advert_detail(request, advert_id):
    advert = get_object_or_404(Home, pk=home_id)
    seller_id = home.user_id  
    return render(request, 'advert_detail.html', {'advert': advert, 'seller_id': seller_id})



def advert_detail(request, advert_id):
    advert = get_object_or_404(Home, pk=advert_id)
    recipient_id = advert.user_id  # Get the ID of the home author's owner
    return render(request, 'advert_detail.html', {'advert': advert, 'recipient_id': recipient_id})

@login_required
def compose_message(request, recipient_id):
    try:
        recipient = get_object_or_404(User, pk=recipient_id)
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message_content = form.cleaned_data['message']
                message = Message(sender=request.user, recipient=recipient, subject=subject, message=message_content)
                message.save()
                messages.success(request, 'Message sent successfully.')
                return redirect('/')  # Redirect to home page after sending message
            else:
                messages.error(request, 'Failed to send message. Please check the form.')
        else:
            form = MessageForm()
        return render(request, 'compose_message.html', {'form': form, 'recipient_id': recipient_id})
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
        return redirect('/')  # Redirect to home page in case of error


@login_required
def unread_message_count(request):
    unread_count = Message.objects.filter(recipient=request.user, is_read=False).count()
    return unread_count

@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    return render(request, 'message_detail.html', {'message': message})

@login_required
def read_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if message.recipient == request.user:
        message.is_read = True
        message.save()
        return render(request, 'message_detail.html', {'message': message})
    else:
        # Handle unauthorized access to messages
        return HttpResponseForbidden("You don't have permission to access this message.")

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.method == 'POST' and message.recipient == request.user:
        message.delete()
        return redirect('inbox')
    return render(request, 'confirm_delete.html', {'message': message})

@login_required
def edit_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.method == 'POST' and message.recipient == request.user:
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('inbox')
    else:
        form = MessageForm(instance=message)
    return render(request, 'edit_message.html', {'form': form, 'message': message})

def inbox(request):
    # Retrieve all messages for the current user
    messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'inbox.html', {'messages': messages})

def SignupView(request):
    # Your signup logic goes here
    return render(request, 'signup.html')