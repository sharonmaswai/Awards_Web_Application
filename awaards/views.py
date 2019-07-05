from django.shortcuts import render, redirect
from .models import Profile, Project, Rating
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ProjectForm, RateForm

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
            profile.username = current_user
            profile.user=current_user.id
            profile.save()

        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile-form.html', {"form":form})

@login_required(login_url='/accounts/login/')    
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user.id)
    print(profile)
    project= Project.objects.all()
    
    return render(request,'profile.html',{'profile':profile,'project':project})
@login_required(login_url='/accounts/login/')
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
@login_required(login_url='/accounts/login/')
def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects':projects}) 
@login_required(login_url='/accounts/login/')
def search_results(request):
    
    if 'search_project' in request.GET and request.GET['search_project']:
        search_term=request.GET.get('search_project')
        
        searched_item=Project.search_project(search_term)
        
    return render(request,'search.html',{'searched_item':searched_item})  
@login_required(login_url='/accounts/login/')
def rate(request,id):
    
    project=Project.objects.get(id=id)
    current_user = request.user
   
    ratings=Rating.objects.filter(project_id=project.id)
   
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            project_rating = form.save(commit=False)
            project_rating.average_vote=round((project_rating.usability + project_rating.content+ project_rating.design)/3)
            project_rating.project=project
            project_rating.user=current_user
            project_rating.save()
            return redirect('projects')
    else: 
        form=RateForm()
    
    return render(request, 'rating.html', {'form':form, 'project':project})
@login_required(login_url='/accounts/login/')
def rate_project(request,project_id):
   
    projects=Project.objects.filter(id=project_id)
    ratings=Rating.objects.filter(project_id=projects)
    average_rating=[]
    mean_rate=0
        
    for rating in ratings:
        average_rating.append(rating.average_vote)
            
    total_rates=sum(average_rating)
    if len(ratings)>0:
        total_rating=total_rates/len(ratings)
        mean_rate=total_rating
    else:
        total_rating=0
        mean_rate=total_rating  
    
    return render(request, 'single-project.html',{'projects':projects,'mean_rate':mean_rate})
