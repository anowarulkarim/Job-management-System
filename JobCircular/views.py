from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from . models import Circular,Recruter
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
class recrutersignup(forms.Form):
    name=forms.CharField(max_length=30)
    company=forms.CharField(max_length=50)
    designation=forms.CharField(max_length=20)
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)
    password2=forms.CharField(max_length=20)
class recruterlogin(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)
class job(forms.Form):
    titel=forms.CharField(max_length=50)
    salary=forms.IntegerField()
    last_date=forms.DateField()
def alljobs(request):
        if request.session.get("login"):
            Circulars=Circular.objects.all()
            return render(request,"JobCircular/jobs.html",{
                "all_jobs":Circulars
        })
        else:
            return redirect(reverse('client_user:login'))
def postjob(request):
    if request.method=="POST":
        job_form=job(request.POST)
        if job_form.is_valid():
            job_recruter=Recruter.objects.get(username=request.session.get("recruter"))
            print(job_recruter)
            new_circular=Circular(
                recruter=job_recruter,
                company=job_recruter.company,
                titel=job_form.cleaned_data["titel"],
                salary=job_form.cleaned_data["salary"],
                last_date=job_form.cleaned_data["last_date"]
            )
            new_circular.save()
                
    if request.session.get("recruter")!=None:
        return render(request,"JobCircular/jobpost.html",{
            "form":job()
        })
    else:
        return redirect(reverse('jobs:recruterlogin'))
def recruterLogin(request):
    if request.method=="POST":
        login_form=recruterlogin(request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data["username"]
            if Recruter.objects.filter(username=username).exists():
                recruter=Recruter.objects.get(username=username)
                password=login_form.cleaned_data["password"]
                if check_password(password, recruter.password):
                    request.session["recruter"]=recruter.username
                    return redirect(reverse('jobs:recruterhome'))
                else:
                    return render(request,"JObCircular/recruterlogin.html",{
                        "form":login_form,
                        "error":"Wrong password"
                    })
            else:
                return render(request,"JObCircular/recruterlogin.html",{
                    "form":login_form,
                    "error":"User Does Not exist"
                })

    return render(request,"JObCircular/recruterlogin.html",{
        "form":recruterlogin()
    })
def recruterSignup(request):
    if request.method=="POST":
        signup_form=recrutersignup(request.POST)
        if signup_form.is_valid():
            username=signup_form.cleaned_data["username"]
            if Recruter.objects.filter(username=username).exists():
                return render(request,"JobCircular/recrutersignup.html",{
                    "form":recrutersignup(),
                    "error":"username Taken"
                })
            elif signup_form.cleaned_data["password"] != signup_form.cleaned_data["password2"]:
                return render(request,"JobCircular/recrutersignup.html",{
                    "form":recrutersignup(),
                    "error":"Password does not match"
                })
            else:
                hashed_password = make_password(signup_form.cleaned_data["password"])
                new_user = Recruter(
                    name=signup_form.cleaned_data["name"],
                    company=signup_form.cleaned_data["company"],
                    designation=signup_form.cleaned_data["designation"],
                    username=username,
                    password=hashed_password,
                )
                new_user.save()
                return redirect(reverse('jobs:recruterlogin'))
        # return redirect(reverse('jobs:recruterlogin'))
    else:
        return render(request,"JobCircular/recrutersignup.html",{
            "form":recrutersignup()
        })
def recruterhome(request):
    if request.session.get("recruter")!=None:
        return render(request,"JobCircular/recruterhome.html")
    else:
        return redirect(reverse('jobs:recruterlogin'))