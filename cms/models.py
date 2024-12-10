from django.db import models


 #slider Table
class Slider(models.Model):
  title = models.CharField(max_length=100, blank=True, null=True)
  image = models.ImageField(upload_to='slider/', blank=True, null=True)
  serial_no = models.IntegerField(blank=True, null= True)
  is_available = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  class Meta:
        verbose_name_plural = "Sliders"

  def __str__(self):
        return f"{self.title}"

 #Project Table
 
CATAGORY_CHOICE = (
("ready", "Ready"),
("ongoing", "Ongoing"),
("upcoming", "Upcoming"),
)

class Project(models.Model):
  catagory_choice = models.CharField(choices= CATAGORY_CHOICE, default="ready", max_length=100)
  name= models.CharField(max_length=100, blank=True, null=True)
  thumbnail_image = models.ImageField(upload_to='project_photo/', blank=True, null=True)
  first_image = models.ImageField(upload_to='project_photo/', blank=True, null=True)
  second_image = models.ImageField(upload_to='project_photo/', blank=True, null=True)
  third_image = models.ImageField(upload_to='project_photo/', blank=True, null=True)
  thumbnail_image = models.ImageField(upload_to='project_photo/', blank=True, null=True)
  description = models.TextField(max_length=1000, blank=True, null = True )
  address = models.TextField(max_length=1000, blank=True, null = True )
  architect_name = models.CharField(max_length=100, blank=True, null = True)
  land_area = models.CharField(max_length=100, blank=True, null = True)
  Specialty_of_the_land = models.CharField(max_length=100, blank=True, null = True)
  total_floor = models.CharField(max_length=100, blank=True, null = True)
  total_apartments = models.CharField(max_length=100, blank=True, null = True)
  unit_size = models.CharField(max_length=100, blank=True, null = True)
  road_width = models.CharField(max_length=100, blank=True, null = True)
  total_basements = models.CharField(max_length=100, blank=True, null = True)
  total_parking = models.CharField(max_length=100, blank=True, null = True)
  approval_no = models.CharField(max_length=100, blank=True, null = True)
  serial_no = models.IntegerField(blank=True, null = True)
  is_available = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
        verbose_name_plural = "Projects"

  def __str__(self):
        return f"{self.name}"
  
  
   #AboutUs Table
class AboutUs(models.Model):
    title = models.CharField(max_length=100, blank=True, null = True)
    description = models.TextField(max_length=1000, blank=True, null = True )
    image = models.ImageField(upload_to='about_photo/', blank=True, null = True)

    class Meta:
        verbose_name_plural = "About Us"

    def __str__(self):
        return f"{self.title}"


   #SisterConcern Table
class SisterConcern(models.Model):
    name = models.CharField(max_length=100, blank=True, null = True)
    photo = models.ImageField(upload_to='team_photo/', blank=True, null = True)
    
    
   #Team Table
class Team(models.Model):
    name = models.CharField(max_length=100, blank=True, null = True)
    designation = models.CharField(max_length=100, blank=True, null = True)
    photo = models.ImageField(upload_to='team_photo/', blank=True, null = True)
    
   #Conuter Table
class Counter(models.Model):
    total_ready_projects = models.CharField(max_length=100, blank=True, null = True)
    total_achievement = models.CharField(max_length=100, blank=True, null = True )
    total_upcoming_projects = models.CharField(max_length=100, blank=True, null = True )
  
   #blog Table
class Blog(models.Model):
    writer = models.CharField(max_length=100, blank=True, null = True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, null = True)
    description = models.TextField(max_length=1000, blank=True, null = True )
    image = models.ImageField(upload_to='project/', blank=True, null = True)   
    serial_no = models.IntegerField(blank=True, null = True)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
        return f"{self.title}"
 
 
    #company info Table     
class CompanyInfo(models.Model):
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null = True)
    address = models.CharField(max_length=100, blank=True, null = True)
    primary_phone = models.CharField(max_length=100, blank=True, null = True)
    secondary_phone = models.CharField(max_length=100, blank=True, null = True)
    email = models.CharField(max_length=100, blank=True, null = True)
    
    facebook_link = models.CharField(max_length=100, blank=True, null = True)
    youtube_link = models.CharField(max_length=100, blank=True, null = True)
    instagram_link = models.CharField(max_length=100, blank=True, null = True)

    class Meta:
        verbose_name_plural = "Company Informations"

    def __str__(self):
        return f"{self.company_name}"

class ContactUs(models.Model):
    name = models.CharField(max_length=100, blank=True, null = True)
    email = models.CharField(max_length=100, blank=True, null = True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField(max_length=1000, blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f"{self.name}"
