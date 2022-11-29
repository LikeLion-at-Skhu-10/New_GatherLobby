from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommunityForm, CommentForm
from .models import Community, Comment

# Create your views here.
def community(request):
    return render(request, "community.html")

def community_write(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.title=request.POST['title']
            form.save()
            return redirect("community.html")
    else:
        form = CommunityForm()
    return render(request, "community_write.html" , {'form' : form})

def community_read(request):
    communitys = Community.objects
    return render(request, "community_read.html",{'communitys': communitys})

def community_detail(request ,id):
    community = get_object_or_404(Community, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            reply = form.save(request.POST)
            reply.community_id = community
            reply.text = form.cleaned_data['text']
            reply.save()
            return redirect('community_detail', id)
    else:
        form = CommentForm()
        return render(request, "community_detail.html", {'community':community, 'form':form})

def community_edit(request, id):
    lobby = get_object_or_404(Community, id=id)
    if request.method == "POST":
        form =CommunityForm (request.POST, request.FILES, instance=community)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('community_read')

    else:
        form =CommunityForm(instance=lobby)
    return render(request, "community_edit.html", {'form':form})

def community_delete(request,id):
    community = get_object_or_404(Community, id=id)
    community.delete()
    return redirect('community_read')