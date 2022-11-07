from django.shortcuts import render, redirect, get_object_or_404
from .forms import LobbyForm , ReplyForm
from .models import Lobby, Reply

# Create your views here.
def introduce(request):
    return render(request, "introduce.html")

def lobby(request):
    return render(request, "lobby.html")

def lobby_write(request):
    if request.method == 'POST':
        form = LobbyForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.title=request.POST['title']
            form.save()
            return redirect('introduce')
    else:
        form = LobbyForm()
    return render(request, "lobby_write.html" , {'form' : form})

def lobby_read(request):
    lobbys = Lobby.objects
    return render(request, "lobby_read.html", {'lobbys':lobbys})

def lobby_detail(request ,id):
    lobby = get_object_or_404(Lobby, id=id)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(request.POST)
            reply.lobby_id = lobby
            reply.text = form.cleaned_data['text']
            reply.save()
            return redirect('lobby_detail', id)
    else:
        form = ReplyForm()
        return render(request, "lobby_detail.html", {'lobby':lobby, 'form':form})

def lobby_edit(request, id):
    lobby = get_object_or_404(Lobby, id=id)
    if request.method == "POST":
        form =LobbyForm (request.POST, request.FILES, instance=lobby)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('lobby_read')

    else:
        form =LobbyForm(instance=lobby)
    return render(request, "lobby_edit.html", {'form':form})

def lobby_delete(request,id):
    lobby = get_object_or_404(Lobby, id=id)
    lobby.delete()
    return redirect('lobby_read')

def lobby_chat(request):
    return render(request, "lobby_chat.html")