from django.urls import path
from . import views
app_name="jobs"
urlpatterns=[
    path("",views.alljobs,name="allJobs"),
    path("postjob/",views.postjob,name="postjob"),
    path("recruterlogin/",views.recruterLogin,name="recruterlogin"),
    path("recrutersignup/",views.recruterSignup,name="recrutersignup"),
    path("recruterpanel/",views.recruterSignup,name="recrutersignup"),
    path("recruterhome/",views.recruterhome,name="recruterhome"),
    path("recruterlogout/",views.recruterlogout,name="recruterlogout"),
    path('apply-job/<int:job_id>/', views.apply_job, name='apply_job'),
]