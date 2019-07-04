from django.db import models
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator
from django.dispatch import receiver
from django.contrib.auth.models import User 
from tinymce.models import HTMLField
from url_or_relative_url_field.fields import URLOrRelativeURLField


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    profile_pic = models.ImageField(default='image.png',upload_to='profiles/')
    bio = HTMLField(max_length=500,default='About me')
    phone_number = models.CharField(max_length=10,default=000000)
    website = URLOrRelativeURLField() 
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
        
    def update_profile(self):
        self.update()
        
    @classmethod
    def search_profile(cls,username):
        profile=Profile.objects.filter(user_id=username)
        
        return profile

    
    def __str__(self):
        return self.bio
class Project(models.Model):
    profile = models.ForeignKey(User,null=True,on_delete=models.CASCADE) 
    title = models.CharField(max_length=100)
    description = models.TextField()
    #technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to="projects/")
    # usability=models.IntegerField(default=0)
    # design=models.IntegerField(default=0)

    # content=models.IntegerField(default=0)
    link = URLOrRelativeURLField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def search_by_projects(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        print(projects)
        return projects 
    
    @classmethod
    def get_profile_projects(cls,profile):
       projects = Projects.objects.filter(profile__pk=profile)
       print(projects)
       return projects
    @classmethod   
    def search_project(cls, search_term):
        
        searched_item=Project.objects.filter(title__icontains=search_term)
        return searched_item
        
    
    def __str__(self):
        return self.title
class Rating(models.Model):
    design = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    usability = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    content = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)]) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    average_vote=models.FloatField(default=0)
    project = models.ForeignKey(Project)
    
    def save_rating(self):
       
        self.save()
        
    def delete_rating(self):
        
        self.delete()
        
    def update_rating(self):
       
        self.update()
        
   
    def __str__(self):
        return self.name