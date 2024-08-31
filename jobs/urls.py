from django.urls import path
from . import views
from clientUser import views as client_views
app_name="jobs"
urlpatterns=[
    path("",views.alljobs,name="alljobs"),
]    