from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'Home.html', {'products': products})


def category(request, foo):
    # replace hyphen with spaces
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, ('that category does not exist'))
        return redirect('Home')


def about(request):
    return render(request, 'about.html', {})

def category_summary(request):
    categories = Category.objects.all()
    return render(request,'category_summary.html',{"categories": categories})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(request, username=username, password=password)
        if User is not None:
            login(request, User)
            messages.success(request, 'you have been logged in')
            return redirect('Home')
        else:
            messages.error(request, 'There was an error, please try again later')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'you are currently logged out,would you like to log in')
    return redirect('Home')


def register_user(request):
    form = SignUpForm(request)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'you have ')
            return redirect('Home')
        else:
            messages.success(request, 'There was an error, please try again later')
            return redirect('register_user')
    else:
        return render(request, 'register.html', {})

    return render(request, 'register.html', {})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {'product': product})
