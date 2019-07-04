from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    
    url('^$',views.index,name='index'),
    url(r'^createprofile/', views.create_profile, name='profile-form'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^upload/', views.upload_project, name='upload'),
    url(r'^projects/', views.projects, name='projects')
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
