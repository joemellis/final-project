from django.urls import path
from . import views
from .views import search_results
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('search/', search_results, name='search_results'),
    path('', views.index,name ='index'),
    path('create-advert/', views.create_advert, name='create_advert'),
    path('success/', views.success_page, name='success_url'),
    path('user/posts/', views.user_posts, name='user_posts'),
    path('user/posts/<int:advert_id>/edit/', views.edit_advert, name='edit_advert'),
    path('user/posts/<int:advert_id>/delete/', views.delete_advert, name='delete_advert'),
    path('compose/<int:recipient_id>/', views.compose_message, name='compose_message'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

    
    
]


