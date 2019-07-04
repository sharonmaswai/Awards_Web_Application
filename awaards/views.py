from django.shortcuts import render, redirect
from .models import Profile, Project
from django.contrib.auth.models import User
from .forms import ProfileForm, ProjectForm

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects':projects}) 
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
    project= Project.objects.all()
    
    return render(request,'profile.html',{'profile':profile,'project':project})
def upload_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            print()
            index= form.save()
            
        return redirect('index')
    else:
        form =ProjectForm()
            
    return render(request,'project-upload.html',{"form":form,})
def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects':projects}) 
def search_results(request):
    
    if 'search_project' in request.GET and request.GET['search_project']:
        search_term=request.GET.get('search_project')
        
        searched_item=Project.search_project(search_term)
        
    return render(request,'search.html',{'searched_item':searched_item})  
def rate(request,id):
    
    project=Project.objects.get(id=id)
    current_user = request.user
   
    ratings=Rating.objects.filter(project_id=project.id)
   
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
        
           
            project_rating = form.save(commit=False)
            
           
            project_rating.average_vote=round((user_rating.usability_vote + user_rating.content_vote + user_rating.design_vote)/3)
            
            
            project_rating.project=project
            
            project_rating.user=current_user
            
            project_rating.save()
            return redirect('projects')
    else: 
        rateform=RatingForm()
    
    return render(request, 'rating.html', {'rateform':rateform, 'project':project})
