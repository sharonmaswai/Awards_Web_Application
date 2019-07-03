from django import forms
from .models import Profile,Projects


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('title','image','description', 'link')
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','bio','website') 