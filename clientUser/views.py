from django import forms
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import redirect, render
from . models import ClientUser
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
class SignUp(forms.Form):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    username=forms.CharField(max_length=20)
    profile=forms.ImageField(required=False)
    resume=forms.FileField(required=False)
    password=forms.CharField(max_length=20, widget=forms.PasswordInput)
    
class Login(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)


def login_view(request):
    if request.method=="POST":
        login_form=Login(request.POST)
        if login_form.is_valid():
            if ClientUser.objects.filter(username=login_form.cleaned_data["username"]).exists():
                user=ClientUser.objects.get(username=login_form.cleaned_data["username"])
                password=login_form.cleaned_data["password"]
                if check_password(password, user.password):
                    request.session["login"]=user.username
                    return redirect(reverse('client_user:home'))
                else:
                    return render(request,"clientUser/login.html",{
                        "form":login_form,
                        "message": "password is not currect"
                    })
            else:
                return render(request,"clientUser/login.html",{
                    "form":login_form,
                    "message": "user does not exist"
                })
        else:
            return HttpResponse("already have"+request.session['username'])
    else:
        if 'username' in request.session:
            return redirect(reverse('client_user:home'))
        else:
            return render(request,"clientUser/login.html",{
                "form":Login()
            })

def logout_view(request):
    if request.session.get("login"):
        del request.session["login"]

    return redirect(reverse('client_user:login'))


def signup(request):
    if request.method=="POST":
        signup_form=SignUp(request.POST, request.FILES)
        print("in signup")
        if signup_form.is_valid():
            print("valid form")
            username = signup_form.cleaned_data["username"]
            if ClientUser.objects.filter(username=username).exists():
                return render(request, "clientUser/signup.html", {
                    "form": signup_form,
                    "message": "Username is already taken"
                })
            else:
                if request.POST["password2"]!= signup_form.cleaned_data["password"]:
                    return render(request, "clientUser/signup.html", {
                    "form": signup_form,
                    "message": "Passwords are not matching"
                })
                else:
                    hashed_password = make_password(signup_form.cleaned_data["password"])
                    new_user = ClientUser(
                        first_name=signup_form.cleaned_data["first_name"],
                        last_name=signup_form.cleaned_data["last_name"],
                        username=username,
                        password=hashed_password,
                        profile=signup_form.cleaned_data["profile"],
                        resume=signup_form.cleaned_data["resume"]
                    )
                    try:
                        new_user.save()
                    except Exception as e:
                        print(f"Error saving new user: {e}")
                    return render(request,"clientUser/login.html",{
                        "form":Login()
                    })

    return render(request,"clientUser/signup.html",{
        "form":SignUp()
    })


def home(request):
    keys = request.session.keys()
    if request.session.get("login"):
        print(request.session.get("login"))
        return render(request, "clientUser/home.html")
    else:
        return render(request,"clientUser/login.html",{
            "form": Login(),
            "message": "You Need To Login First"
            })

def show_profile(request):
    if request.session.get("login"):
        user=ClientUser.objects.get(username=request.session["login"])
        print(user.profile)
        print(user.profile.url)
        print(user.profile.path)
        return render(request,"clientUser/profile.html",{
            "user": user
        })
    else:
        return render(request,"clientUser/login.html",{
            "form": Login(),
            "message": "You Need To Login First"
            })