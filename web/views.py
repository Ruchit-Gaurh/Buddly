from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    if request.user.is_authenticated:
        return redirect("/home")
    return render(request, 'index.html')

@login_required(login_url="/login_page")
def home(request):
    user = request.user.profile
    context= {'user':user}
    return render(request, 'home.html', context)

def register_page(request):
    if request.user.is_authenticated:
        return redirect("/home")
    context = {}
    return render (request, "register.html", context)

def register(request):
    username= request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    User.objects.create_user(str(username), str(email), str(password))
    user = User.objects.get(username=username)
    print(user)
    fname = request.POST['name']
    url = request.POST['url']
    if url :
        purl = url
    else:
        purl = "https://cdn-icons-png.flaticon.com/512/666/666201.png"
    ch = Profile.objects.create(user=user, name=fname, pic=purl)
    return redirect("/login_page")

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/home")
    context = {}
    return render(request, "login.html", context)

def loginn(request):
    name = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=name, password= password)
    if user is not None:
        login(request, user)
        return redirect('/home')
    else:
        return HttpResponse("<h2>Kyu rakhte ho aaisa password jo yaad hi na rhe<h2>")


def chat(request):
    user = request.user.profile
    context= {'user':user}
    return render (request, "chat.html", context)