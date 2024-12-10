from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'), 
    path('AboutUs/', views.about_us, name='about_us'),    
    path('All-Project/', views.all_projects, name='all_projects'),    
    path('Ready-Project/', views.ready_projects, name='ready_projects'),    
    path('Ongoing-Project/', views.ongoing_projects, name='ongoing_projects'),    
    path('Upcoming-Project/', views.upcoming_projects, name='upcoming_projects'),
    path('blog/', views.blog, name='blog'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('project/<int:id>', views.get_projects, name='get_projects'), 
    path('blog/<int:id>', views.get_blogs, name='get_blogs'), 
]