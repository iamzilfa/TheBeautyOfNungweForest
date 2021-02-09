from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Photo,Comments
from django.contrib.auth.decorators import login_required
from .forms import NewPhotoForm,NewProfileForm,CommentForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request):
    ones_photo = Photo.objects.all()
    all_photos = Photo.get_all_photo()
    return render(request, 'index.html', {"all_photos": all_photos, "ones_photo":ones_photo})

# @login_required(login_url='/accounts/login/')
def upload_photo(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')

    else:
        form = NewPhotoForm()
    return render(request, 'post_photo.html', {"form": form}) 


@login_required(login_url='accounts/login/')
def add_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id = current_user.id)
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.user = current_user
            caption.save()
            return redirect('myprofile')
    else:
        form = NewProfileForm()
    return render(request, 'edit_profile.html', {"form":form})    


@login_required(login_url='accounts/login/')
def my_profile(request):
    current_user = request.user
    my_projects = Photo.objects.filter(user = current_user)
    my_profile = Profile.objects.filter(user = current_user).first
    return render(request, 'profile.html', {"my_projects": my_projects, "my_profile":my_profile})


@login_required(login_url='/accounts/login/')
def search_photo(request):
    if 'photo_name' in request.GET and request.GET["photo_name"]:
        search_term = request.GET.get("photo_name")
        searched_photo = Photo.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, "search.html",{"message":message,"photo": searched_photo})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})



@login_required(login_url='/accounts/login/')
def add_comment(request, proj_id):
    current_user = request.user
    photo_item = Photo.objects.filter(id = proj_id).first()
    profiless = Profile.objects.filter(user = current_user.id).first()
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posted_by = profiless
            comment.commented_photo = photo_item
            comment.save()
            return redirect('onephoto', proj_id)
    else:
        form = CommentForm()
    return render(request, 'review_form.html', {"form": form, "proj_id": proj_id})


@login_required(login_url='/accounts/login/')
def comment(request, id):
    mycomments = Comments.objects.filter(commented_photo = id).all()
    return render(request, 'reviews.html', {"mycomments":mycomments})

def one_photo(request,id):
    ones_photo = Photo.objects.filter(id = id)
    return render(request,'photo.html',{"ones_photo":ones_photo,})

def likes(request,id):
   likes=0
   photo = Photo.objects.get(id=id)
   photo.likes = photo.likes+1
   photo.save()
   
   return redirect('onephoto', id)
