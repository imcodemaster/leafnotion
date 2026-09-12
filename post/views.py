from django.shortcuts import render
from .models import * 
from django.shortcuts import get_object_or_404
from accounts.models import UserProfile
#from django.contrib.auth.decorators import login_required
 # importing class based views from views.generic
from django.views.generic import View, ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin #importing loginrequiredMixin and UserPassesTestMixin from auth.mixin
from django.contrib.auth.models import User #import User from models
from django.urls import reverse_lazy , reverse
from django.views.generic.edit import FormView
from .forms  import PostForm , PostCommentForm , PostUpdateForm , VideoForm , VideoCommentForm
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .render import Render
from django.views import View
from accounts.models import *




def LikeView(request , pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    got_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        got_liked = False
    else:
        post.likes.add(request.user)
        got_liked = True
    return HttpResponseRedirect(reverse('post-detail' , args=[str(pk)]))





def VideoLikeView(request , pk):
    videos = get_object_or_404(video, id=request.POST.get('video_id'))
    got_liked = False
    if videos.likes.filter(id=request.user.id).exists():
        videos.likes.remove(request.user)
        got_liked = False
    else:
        videos.likes.add(request.user)
        got_liked = True
    return HttpResponseRedirect(reverse('video-detail' , args=[str(pk)]))


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post/post_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'post' , 'user', 'Story' 
    ordering = ['-published']



class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'post/post_detail.html' #<app>/<model>_<viewtype>.html
    
    def get_context_data(self , *args , **kwargs):
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        got_liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            got_liked = True

        context = super(PostDetailView , self).get_context_data( *args , **kwargs)
        context ['objects_name'] = 'post'
        context ['total_likes'] = total_likes
        context ['got_liked'] = got_liked
        return context
    



class VideoDetailView(LoginRequiredMixin,DetailView):
    model = video
    template_name = 'post/video_detail.html' #<app>/<model>_<viewtype>.html
    
    def get_context_data(self , *args , **kwargs):
        stuff = get_object_or_404(video, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        got_liked = False
        
        if stuff.likes.filter(id = self.request.user.id).exists():
            got_liked = True
        context = super(VideoDetailView , self).get_context_data( *args , **kwargs)
        context ['objects_name'] = 'video'
        context ['total_likes'] = total_likes
        context ['got_liked'] = got_liked
        return context




class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post #describing models 
    template_name = 'post/post_form.html' #<app>/<model>_<viewtype>.html
    #context_objects_name = 'think'
    #fields = ['content' , 'feeling', 'activity', 'image']#describe the field need to create
    form_class = PostForm 
    success_url = reverse_lazy('post-list')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView,):
    model = Post
    form_class = PostUpdateForm 
    template_name = 'post/post_update_form.html'
    #fields = ['content' , 'feeling', 'activity', 'image']
    #describe the field need to Update
    success_url = reverse_lazy('post-list')
    
    def form_valid(self,form):

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False 

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,):
    model = Post
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 



def usersearch(request):

    try:
        query = request.GET.get('queryuser')
    except:
        query = None

    if query :
        query = request.GET.get('queryuser').lower()
        template = 'post/postresults.html'
        result = [item for item in User.objects.filter(first_name__icontains = query) if query in item.first_name.lower()]



    else:
        template = 'post/post-list.html'
        result = {}

    return render(request, template, {"result": result })





class VideoListView(LoginRequiredMixin, ListView):
    model = video
    template_name = 'post/video_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'Video' , 'user'
    ordering = ['-published']
    paginate_by = 10



class VideoCreateView(LoginRequiredMixin, CreateView):
    model = video #describing models 
    form_class = VideoForm
    template_name = 'post/video_form.html'
    #fields = [ 'subject' ,  'video' ] #describe the field need to create 
    success_url = reverse_lazy('video-list')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class VideoDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,):
    model = video
    success_url = reverse_lazy('video-list')

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.author:
            return True
        return False 


#=================================================
class PostCommentCreateView(LoginRequiredMixin, CreateView):
    model = PostComment #describing models 
    form_class = PostCommentForm 
    #fields = ['comment_content' , 'reaction'] #describe the field need to create 
    ordering = ['published']
    template_name = 'post/postcomment_form.html'
    success_url = reverse_lazy('post-list' ) 

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)



class VideoCommentCreateView(LoginRequiredMixin, CreateView):
    model = VideoComment #describing models 
    form_class = VideoCommentForm 
    #fields = ['comment_content'] #describe the field need to create 
    #ordering = ['published']
    template_name = 'post/videocomment_form.html'
    success_url = reverse_lazy('video-list')

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)




class ProfilepdfView(View):

    def get(self, request):
        personprofile = UserProfile.objects.filter(user = request.user)
        today = timezone.now()
    
        params = {
            'today': today,
            'personprofile': personprofile,
            'request': request
            }
        return Render.render( '../templates/accounts/profile_pdf.html',  params)    


