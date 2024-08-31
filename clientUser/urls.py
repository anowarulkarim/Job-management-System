from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from job_management_system import settings
from . import views
app_name="client_user"
urlpatterns=[
    path("",views.login_view,name="login"),
    path("signup/",views.signup,name="signup"),
    path("home/",views.home, name="home"),
    path("logout/",views.logout_view, name="logout"),
    path("showProfile/",views.show_profile, name="show_profile")
]