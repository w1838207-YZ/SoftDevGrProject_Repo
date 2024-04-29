from django.urls import path
from . import views


urlpatterns = [
    
    #General web pages
    
    path('', views.home),
    path('blist/', views.blist),
    path('navbar/', views.navbar),
    path('login/', views.user_login, name='login'),
    path('admin_login/', views.user_admin_login, name='admin_login'),
    path('sign_up/', views.user_sign_up, name='sign_up'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('contactus/', views.contact_us, name='contactus'),
    
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
