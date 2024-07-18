
from django.contrib import admin
from django.urls import path
from EstateAgencyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('agentsingle/', views.agentsingle,name='agentsingle'),
    path('agentsgrid/', views.agentsgrid,name='agentsgrid'),
    path('bloggrid/', views.bloggrid,name='bloggrid'),
    path('blogsingle/', views.blogsingle,name='blogsingle'),
    path('contact/', views.contact,name='contact'),
    path('propertygrid/', views.propertygrid,name='propertygrid'),
    path('propertysingle/', views.propertysingle,name='propertysingle'),

]
