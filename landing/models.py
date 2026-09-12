'''
Learnincreation model - main website


'''
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.



# Create your models here.

Department = [
                ('Support & Helpdesk Department', "Support & Helpdesk Department"),
                ('Report & Feedback Department', "Report & Feedback Department"),
                ('Customer Support Department', "Customer Support Department"),
                ('In-appropiate Content Report', "In-appropiate Content Report"),
                ('Other Reason', "Other Reason"),
                
        ]

subscribefor = [
                ('Build Business Profile', "Build Business Profile"),
                ('Free E-books & Updates', "Free E-books & Updates"),
                ('Free Sessions & Newsletter', "Free Sessions & Newsletter"),
                ('Send me all Updates', "Send me all Updates"),
            
        ]



#contact model for front end 

class Contact(models.Model):
    first_name = models.CharField(max_length = 100)
    second_name = models.CharField(max_length = 100)
    to_the_department = models.CharField( max_length = 30 , choices=Department , null=True , blank=True)
    email = models.EmailField() 
    mobile = models.CharField(max_length = 10)
    message = models.TextField()
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.first_name 



'''

# teacher model - faculty view

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(null = True , blank = True)
    img = models.ImageField(null = True, blank = True)
    qualification = models.CharField(max_length=200)
    salary = models.FloatField()
    age = models.IntegerField()
    phonenumber = models.IntegerField() #without country code
    aadaharid = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)
	#slug = models.SlugField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self): #imgUrl ke media se lelega .. /media/ wala
        try :
            url = self.img.url
        except:
        	url = ''
        return url

# department model - (dynamic department updation)

class Department(models.Model):
    name = models.CharField(max_length = 100)
    Subject_name1 = models.CharField(max_length = 100 , null = True , blank = True)
    Subject_name2 = models.CharField(max_length = 100 ,null = True , blank = True)
    Subject_name3 = models.CharField(max_length = 100 , null = True , blank = True)
    Subject_name4 = models.CharField(max_length = 100 ,null = True , blank = True)
    Subject_name5 = models.CharField(max_length = 100 , null = True , blank = True)
   
    hod_msg = models.TextField(null = True , blank = True)
    
    about = models.TextField(null = True , blank = True)
    hod_name =models.CharField(max_length= 50 , null = True , blank = True)
    hod_email = models.CharField(max_length = 50, null = True , blank = True)
    branch = models.CharField(max_length = 30 , null = True , blank = True )
 

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def mediaURL(self):
        try : 
            url = self.img.url
        except : 
            url = ''
        return url 

#our pride model  - encouragement view - 

class Pride(models.Model):
    student = models.CharField(max_length=100)
    detail = models.TextField(null = True , blank = True)
    img = models.ImageField(null = True, blank = True)
    qualification = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add = True)
    #slug = models.SlugField()

    def __str__(self):
        return self.student

    @property
    def imageURL(self):
        try :
            url = self.img.url
        except:
            url = ''
        return url


'''


class Subscribe(models.Model):
    
    first_name = models.CharField(max_length = 100)
    second_name = models.CharField(max_length = 100)
    Subscription = models.CharField( max_length = 100 , choices=subscribefor , null=True , blank=True)
    email = models.EmailField() 
    mobile = models.CharField(max_length = 10)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.first_name 



#notice model  - ntioce view  - news front end 
        

class Think(models.Model):
   
    title = models.CharField(max_length = 1000)
    published = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length = 100)
   


    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title
