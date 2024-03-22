from django.urls import path,include
from . import views
from .views import search_results
from django.contrib.auth import views as auth_views
from allauth.account.views import SignupView 
from allauth.account.views import LoginView

urlpatterns =[
    
    path('', views.index,name ='index'),
    path('create-advert/', views.create_advert, name='create_advert'),
   
    path('user/posts/', views.user_posts, name='user_posts'),
    path('user/posts/<int:advert_id>/edit/', views.edit_advert, name='edit_advert'),
    path('user/posts/<int:advert_id>/delete/', views.delete_advert, name='delete_advert'),
    path('compose/<int:recipient_id>/', views.compose_message, name='compose_message'),
    path('account/login.html', LoginView.as_view(), name='login'),
    path('inbox/', views.inbox, name='inbox'),
    path('message/<int:message_id>/', views.read_message, name='read_message'),
    path('message/<int:message_id>/delete/', views.delete_message, name='delete_message'),
    path('message/<int:message_id>/edit/', views.edit_message, name='edit_message'),
    path('message/<int:message_id>/', views.message_detail, name='message_detail'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('accounts/', include('allauth.urls')),
    #path('account/signup/', SignupView.as_view name='login'w(), name='account_signup'),
    path('search/', search_results, name='search'),
  
    
]