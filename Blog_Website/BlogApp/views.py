from django.shortcuts import render
from  .models import *

# Create your views here.

def index(request):
    blogPosts = BlogPost.objects.all()
    aboutMe = AboutMe.objects.all().first()

    return render(request, "index.html", {"blogPosts" : blogPosts, "aboutMe": aboutMe})
