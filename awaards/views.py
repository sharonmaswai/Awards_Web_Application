from django.shortcuts import render, redirect
from .models import Profile, Project
from django.contrib.auth.models import User
from .forms import ProfileForm, ProjectForm

# Create your views here.
def index(request):

    return render(request, 'index.html') 
def create_profile(request):
    
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            # profile.username = current_user
            profile.user=current_user.id
            profile.save()

        return redirect('profile')
    else:
        form = ProfileForm()

    return render(request, 'profile-form.html', {"form":form})
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user.id)
    print(profile)
    project= Project.get_profile_projects(id=project_id)
    
    return render(request,'profile.html',{'profile':profile,'details':details,'project':project})
