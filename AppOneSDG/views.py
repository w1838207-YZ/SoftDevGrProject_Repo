from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from .models import Equipment, Reservation

# Create your views here.

testdata = [
    {'id':1, 'name': 'Item 1 of list'},
    {'id':2, 'name': 'Item 2 of list'},
    {'id':3, 'name': 'Item 3 of list'},
    {'id':4, 'name': 'Item 4 of list'},
    {'id':5, 'name': 'Item 5 of list'},
    {'id':6, 'name': 'Item 6 of list'},
]

def home(request):
    return render(request, 'AppOneSDG/home.html', {'testdata':testdata})

def blist(request):
    return render(request, 'AppOneSDG/blist.html')

def navbar(request):
    return render(request, 'navbar.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home.html')
        else:
            return render(request, 'login.html', {'message': 'Invalid email or password'})
    else:
        return render(request, 'login.html')
    

def user_admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home.html')
        else:
            return render(request, 'admin_login.html', {'message': 'Invalid email or password'})
    else:
        return render(request, 'admin_login.html')


def user_sign_up(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        agree = request.POST.get('agree')

        if password != confirm_password:
            return render(request, 'sign_up.html', {'message': 'Passwords do not match'})

        if not agree:
            return render(request, 'sign_up.html', {'message': 'You must agree to the terms and conditions'})

        #if User.objects.filter(email=email).exists():
            #return render(request, 'sign_up.html', {'message': 'Email already exists'})

        #user = User.objects.create_user(username=email, email=email, password=password)
        #user.first_name = full_name
        #user.save()

        return redirect('/')
    else:
        return render(request, 'sign_up.html')

    
def forgot_password(request):
    message = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # Generate password reset link and send email
            reset_link = "/"  # Replace with actual reset password link
            #send_mail(
                #'Password Reset',
                #f'Click the link to reset your password: {reset_link}',
                #settings.EMAIL_HOST_USER,
                #[email],
                #fail_silently=False,
            #)
            message = 'An email has been sent to reset your password'
        else:
            message = 'Please provide an email address.'
    return render(request, 'forgot_password.html', {'message': message})


def contact_us(request):
    return render(request,"contactus.html")

def sitemap(request):
    return render(request,"sitemap.html")


def currentBookings(request):
    return render(request,"currentBookings.html")

def bookingsHistory(request):
    return render(request,"bookingsHistory.html")


def updateAccountInformation(request):
    return render(request,"updateAccountInformation.html")


#def devices(request):
    #return render(request,"bookingsHistory.html")


def manageBookings(request):
    reservationsToApprove = Reservation.objects.all()
    context = {'reservationsToApprove' : reservationsToApprove}
    return render(request, "manageBookings.html", context)


def manageUsers(request):
    return render(request,"manageUsers.html")


def main_admin(request):
    return render(request,"main_admin.html")

def main_user(request):
    return render(request,"main_user.html")


def devices(request):
    equipments = Equipment.objects.all()
    context = {'equipments' : equipments}
    return render(request, "devices.html", context)

def devicesInventory(request):
    equipments = Equipment.objects.all()
    context = {'equipments' : equipments}
    return render(request,"devices_admin.html", context)

def addProduct(request):
    return render(request,"addProduct.html")


def updateProduct(request):
    return render(request,"updateProduct.html")