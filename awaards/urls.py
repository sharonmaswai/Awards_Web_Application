from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    
    url('^$',views.index,name='index'),
    url(r'^createprofile/', views.create_profile, name='profile-form'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^upload/', views.upload_project, name='upload'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^rate_project/(\d+)/', views.rate_project, name='rate_project'),
    url(r'^rate_form/(\d+)/',views.rate, name='rateform'),
    url(r'^search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
