from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from . models import job
from clientUser import views as clientUserViews
# Create your views here.
def alljobs(request):
    if request.session.get("login"):
        jobs=job.objects.all()
        print(jobs)
        return render(request,"jobs/jobs.html",{
            "all_job":jobs
        })
    else:
        return redirect(reverse('client_user:login'))