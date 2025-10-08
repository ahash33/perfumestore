from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Control
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
@login_required

# Create your views here.
def basic(request):
    return HttpResponse("hello,dgango")

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def collection(request):
    posts=Control.objects.all()
    return render(request,'collections.html',{'post':posts})

def shop(request):
    return render(request,'shop.html')
    
def contact(request):
    return render(request,'contact.html')

def detail(request,post_id):
    post=Control.objects.get(pk=post_id)
    return render(request,'detail.html',{'post':post})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)   # logs in the user
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, "signup.html")

        # check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return render(request, "signup.html")

        # create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # auto-login after signup
        login(request, user)
        return redirect("index")

    return render(request, "signup.html")

# email

# views.py

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f"New Contact Form Submission from {name}"
            full_message = f"Message from {name} ({email}):\n\n{message}"

            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,       # From
                ['ahashahash45@gmail.com'],       # To (your email or list)
                fail_silently=False,
            )
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


# order view
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import OrderForm

def order_perfume(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()

            # Send Gmail notification
            subject = "New Perfume Order Received"
            message = (
                f"Customer: {order.customer_name}\n"
                f"Email: {order.email}\n"
                f"Perfume: {order.perfume_name}\n"
                f"Quantity: {order.quantity}\n"
                f"Address: {order.address}"
            )
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,  # from email
                [order.email, "ahashahash22@gmail.com"],  # to customer + shop owner
                fail_silently=False,
            )

            return redirect("order_success")  # redirect after success
    else:
        form = OrderForm()

    return render(request, "order.html", {"form": form})

def order_success(request):
    return render(request, "order_success.html")
def basic(request):
    return HttpResponse("hello,dgango")