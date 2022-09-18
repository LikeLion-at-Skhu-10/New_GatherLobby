import re
from django.shortcuts import render

# Create your views here.
def community(request):
    return render(request, "community.html")

def community_write(request):
    return render(request, "community_write.html")

def community_read(request):
    return render(request, "community_read.html")

def community_detail(request):
    return render(request, "community_detail.html")

def community_edit(request):
    return render(request, "community.html")