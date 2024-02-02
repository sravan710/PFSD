from django.urls import path
from . import views


urlpatterns = [
path("", views.homepage, name=""),
path("login", views.loginpage, name="login"),
path("contactus", views.contactpage, name="contact"),
path("aboutus", views.aboutpage, name="about"),
#path("ttmhome", views.ttmhome, name="ttmhome"),
path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
]