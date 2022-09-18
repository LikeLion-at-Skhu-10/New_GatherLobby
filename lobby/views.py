from django.shortcuts import render

# Create your views here.
def introduce(request):
    return render(request, "introduce.html")

def lobby(request):
    return render(request, "lobby.html")

def lobby_write(request):
    return render(request, "lobby_write.html")

def lobby_read(request):
    return render(request, "lobby_read.html")

def lobby_detail(request):
    return render(request, "lobby_detail.html")

def lobby_edit(request):
    return render(request, "lobby_edit.html")

def lobby_chat(request):
    return render(request, "lobby_chat.html")