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

def edit_reply(request, id, reply_id):
    post = get_object_or_404(Lobby, id=id)
    reply = get_object_or_404(Reply, id=reply_id)
    form = ReplyForm(instance=reply)
    if request.method == "POST":
        edit_reply_form = ReplyForm(request.POST, instance = reply)
        if edit_reply_form.is_valid():
            edit_reply_form.save()
            return redirect('lobby_detail', id)
    return render(request, 'edit_reply.html', {'form':form, 'post':post, 'reply':reply})

def delete_reply(request, id, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    reply.delete()
    return redirect('lobby_detail',id)

def lobby_delete(request,id):
    lobby = get_object_or_404(Lobby, id=id)
    lobby.delete()
    return redirect('lobby_read')

def lobby_chat(request):
    return render(request, "lobby_chat.html")