from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.
def alljobs(request):
        if request.session.get("login"):
            return render(request,"JobCircular/jobs.html",{
                "all_job":"adfadf"
        })
        else:
            return redirect(reverse('client_user:login'))
    