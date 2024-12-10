from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from cms.models import *
from django.contrib import messages 

def home(request):
  sliders = Slider.objects.first()
  project = Project.objects.all()[:4]
  about_us = AboutUs.objects.first()
  sister_concerns = SisterConcern.objects.all()
  team = Team.objects.all()
  counter = Counter.objects.first()
  blog = Blog.objects.all().order_by('serial_no')[:4]
  company_info = CompanyInfo.objects.first()
  
  context = {
    'sliders' : sliders,
    'project' : project,
    'about_us': about_us,
    'sister_concerns' : sister_concerns,
    'team' : team,
    'counter' : counter,
    'blog' : blog,
    'company_info' : company_info,
  }
  return render(request, 'home/home.html', context)

def about_us(request):
    about_us = AboutUs.objects.first()
    team = Team.objects.all()
    sister_concerns = SisterConcern.objects.all()
    company_info = CompanyInfo.objects.first()

    context = {
        'about_us': about_us,
        'team': team,
        'sister_concerns': sister_concerns,
        'company_info' : company_info,
    }

    return render(request, 'cms/about.html', context)

def all_projects(request):
   
    all_projects =  Project.objects.all()
    company_info = CompanyInfo.objects.first()
   
    context = {  
        'all_projects': all_projects,
        'company_info' : company_info,
    }

    return render(request, 'cms/all_project.html', context)
def ready_projects(request):
   
    ready_projects =  Project.objects.filter(catagory_choice='ready').order_by('serial_no')
    company_info = CompanyInfo.objects.first()
   
    context = {  
        'ready_projects': ready_projects,
        'company_info' : company_info,
    }

    return render(request, 'cms/ready_project.html', context)

def ongoing_projects(request):
   
    ongoing_projects =  Project.objects.filter(catagory_choice='ongoing').order_by('serial_no')
    company_info = CompanyInfo.objects.first()
   
    context = {  
        'ongoing_projects': ongoing_projects,
        'ongoing_info' : company_info,
    }

    return render(request, 'cms/ongoing_project.html', context)

def upcoming_projects(request):
   
    upcoming_projects =  Project.objects.filter(catagory_choice='upcoming').order_by('serial_no')
    company_info = CompanyInfo.objects.first()
   
    context = {  
        'upcoming_projects': upcoming_projects,
        'company_info' : company_info,
    }

    return render(request, 'cms/upcoming_project.html', context)

def get_projects(request, id):
    project_details = Project.objects.get(id=id)
    company_info = CompanyInfo.objects.first()
    context = {
        'project_details': project_details,
        'company_info' : company_info,
    }

    return render(request, 'cms/project-details.html', context)
def blog(request):
   
    blog = Blog.objects.all().order_by('serial_no')
    company_info = CompanyInfo.objects.first()
   
    context = {  
        'blog' : blog,
        'company_info' : company_info,
    }

    return render(request, 'cms/blog.html', context)

def get_blogs(request, id):
    blog_details = Blog.objects.get(id=id)
    company_info = CompanyInfo.objects.first()
    context = {
        'blog_details': blog_details,
        'company_info' : company_info,
    }

    return render(request, 'cms/blog-details.html', context)

def contact_us(request):
    company_info = CompanyInfo.objects.first()
    context = {  
        'company_info' : company_info,
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')  # Get the phone number
        message = request.POST.get('message')

        # Save the data to the database
        ContactUs.objects.create(name=name, email=email, phone=phone, message=message)
        # Add a success message
        messages.success(request, 'Your message has been successfully sent!')

        return redirect('contact_us') 


    return render(request, 'cms/contact.html', context)
