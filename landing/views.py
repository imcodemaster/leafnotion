'''
Learnincreation and Learnincreation geeks run on same domain , learnincreation .co.in
to move in learnincreation login not required , 
however, learnincreation geeks required login details
dynamic e-learning portal
root path - shows search bar - no login need 
show search result 
wanna particular post id access , login required !! _ WELCOME TO LEARNING WORLD 

rest , learnincreation - home, about , product, founder desk (later version update),
contact , notice section (later version update)  (with tooltip)

geeks - include my squad 
geeks detail on geeks app -- 

language detail - new version update

'''
 
#import section ---- 
from django.shortcuts import render
from landing.models import Contact, Think, Subscribe 
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView # importing class based views from views.generic
from django.core.paginator import Paginator
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *

# Create your views here.  

#welcome
def index(request):
	return render(request, 'landing/index.html')


#_website_home_view

def home(request):
    return render(request, 'landing/home.html') 

#think with learnincreation thought section view (notice)

class ThinkListView(ListView): # turns to announcment
    model = Think
    template_name = 'landing/think_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'think'
    ordering = ['-published']
    paginate_by = 10 # pagination  (django provided )


#_website_about _page

def about(request):
	return render(request, 'landing/about.html')


'''
#faculty view - front end 

def faculty(request):
    teacher = Teacher.objects.all()
    context = {'teacher':teacher}
    return render(request, 'landing/faculty.html',context)

#our pride section - front end - for student 

def encouragement(request):
    pride = Pride.objects.all()
    context = {'pride':pride}
    return render(request, 'info/ourpride.html',context)

'''

'''
#campus_details For frontend 

def campus(request):
    return render(request, 'info/ourcampus.html' , context)

def our_department(request):
    department_dynamic = Department.objects.all()
    context = {'department_dynamic':department_dynamic}
    return render(request, 'info/our_department.html' , context)


'''

#contact view for website 

class ContactView(CreateView):
	model = Contact
	fields = ['first_name', 'second_name' , 'to_the_department',  'email' , 'mobile' , 'message' ] #describe the field need to create 
	success_url = reverse_lazy('home')


#gallary ection dynamic view - 

def gallary(request):
	return render(request, 'landing/gallary.html')


#subscribe view


class SubscribeView(CreateView):
	model = Subscribe
	fields = ['first_name', 'second_name' , 'Subscription' , 'email' , 'mobile' ] #describe the field need to create 
	success_url = reverse_lazy('home')





# share your knowledge

def shareyourknowledge(request):
	return render(request, 'landing/campaign.html')




#_website_FAQ _page

def faq(request):
	return render(request, 'landing/faq.html')





# policies

def policies(request):
	return render(request, 'landing/policies.html')

#_website_terms_page

def terms(request):
	return render(request, 'landing/terms.html')



#_website_terms_page

def community(request):
	return render(request, 'landing/community.html')




#_website_helpdesk _page

def helpdesk(request):
	return render(request, 'landing/helpdesk.html')

'''
# geeks-blog-article-list
class businessprofileView(ListView): # turns to announcment
    model = businessProfile
    template_name = 'landing/businessprofile_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'shop'
    ordering = ['-date']
  

class businessprofileCreateView(LoginRequiredMixin, CreateView):
	model = businessProfile
	fields = ['business_name', 'mobile'   , 'snap' , 'email', 'description' , 'sector' , 'location' ] #describe the field need to create 
	success_url = reverse_lazy('business')


# geeks-courses-detail
class businessprofileDetailView(LoginRequiredMixin, DetailView):
	model = businessProfile
	template_name = 'landing/business_detail.html'


class businessprofileUpdateView(LoginRequiredMixin, UpdateView):
	model = businessProfile
	fields = ['business_name', 'mobile'   , 'snap' , 'email', 'description' , 'sector' , 'location' ] #describe the field need to create
	template_name = 'landing/businessprofile_update.html'
	success_url = reverse_lazy('business')


class businessprofileDeleteView(LoginRequiredMixin, DeleteView):
	model = businessProfile
	success_url = reverse_lazy('business')

'''

