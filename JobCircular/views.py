from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from . models import Circular
# Create your views here.
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
    return render(request,"JobCircular/jobpost.html",{
         "form":job()
    })