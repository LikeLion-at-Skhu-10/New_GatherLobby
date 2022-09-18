from django.shortcuts import render

# Create your views here.
def mypage(request):
    return render(request, "mypage.html")

def mypage_write(request):
    return render(request, "mypage_write.html")

def mypage_chat(request):
    return render(request, "mypage_chat.html")