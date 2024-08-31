from django.urls import path
from . import views
app_name="jobs"
urlpatterns=[
    path("",views.alljobs,name="allJobs"),
    path("postjob/",views.postjob,name="postjob")
]