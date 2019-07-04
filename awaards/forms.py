from django import forms
from .models import Profile,Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title','image','description', 'link')
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','bio','website') 
class RateForm(forms.ModelForm):
    class Meta:
        model= Rating
        fields= ('')        