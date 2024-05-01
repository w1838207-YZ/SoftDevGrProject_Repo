from django.urls import path
from . import views
from django.contrib.auth import views as log_views


urlpatterns = [
    
    #General web pages
    path('', views.home, name='home'),
    path('blist/', views.blist),
    path('navbar/', views.navbar),
    path('login/', log_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('admin_login/', log_views.LoginView.as_view(template_name='admin_login.html'), name='admin_login'),
    path('sign_up/', views.user_sign_up, name='sign_up'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('contactus/', views.contact_us, name='contactus'),
    path('logout/', log_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    #Admin web pages
    path('mainAdmin/', views.main_admin, name='mainAdmin'),
    path('manageBookings/', views.manageBookings, name='manageBookings'),
    path('manageUsers/', views.manageUsers, name='manageUsers'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('updateProduct/', views.updateProduct, name='updateProduct'),
    path('devicesInventory/', views.devicesInventory, name='devicesInventory'),
    
    #User web pages
    path('mainUser/', views.main_user, name='mainUser'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('devices/', views.devices, name='devices'),
    path('currentBookings/', views.currentBookings, name='currentBookings'),
    path('updateAccountInformation/', views.updateAccountInformation, name='updateAccountInformation'),
    path('bookingsHistory/', views.bookingsHistory, name='bookingsHistory'),
    
    
    
    
    
    
    
     
]
