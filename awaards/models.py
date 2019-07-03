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
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
     
    @receiver(post_save, sender=User) 
    def save_profile(sender,instance,**kwargs):
        instance.profile.save()  
        
    
    @classmethod
    def get_by_id(cls,id):
        profile = Profile.objects.get(user = id)
        return profile
    
    @classmethod
    def filter_by_id(cls,id): 
        profile = Profile.objects.filter(user = id).first()
        return profile
    
   
    
    def __str__(self):
        return self.bio
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to="projects/")
    usability=models.IntegerField(default=0)
    design=models.IntegerField(default=0)

    content=models.IntegerField(default=0)
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
    
    
    def __str__(self):
        return self.title
class Rating(models.Model):
    design = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    usability = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    content = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)]) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.IntegerField(default=0) 
    