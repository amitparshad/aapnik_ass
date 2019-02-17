from django.shortcuts import render,redirect
from django.contrib.auth import logout

#from .models import Post

# Create your views here.
#for rendering the home page
def home(request):
    return render(request,"home.html")


def log_out(request):
    logout(request)





