from django.urls import path
from post import views 
from .views import *

urlpatterns = [


    path('post/notion/' , PostListView.as_view() , name = "post-list"),
    path('video/' , VideoListView.as_view() , name = "video-list"),
    path('post/notion/<int:pk>/', PostDetailView.as_view() , name = 'post-detail' ),
    path('video/<int:pk>/', VideoDetailView.as_view() , name = 'video-detail' ),
   	path('like/<int:pk>/', LikeView , name = 'post-like' ),
   	path('videolike/<int:pk>/', VideoLikeView , name = 'video-like' ),
 	path('post/notion/new/', PostCreateView.as_view() , name = 'post-create' ),
 	path('video/new/', VideoCreateView.as_view() , name = 'video-create' ),
    path('post/notion/<int:pk>/update/', PostUpdateView.as_view() , name = 'post-update' ),
    path('post/notion/<int:pk>/delete/', PostDeleteView.as_view() , name = 'post-delete' ),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view() , name = 'video-delete' ),
    path('post/notion/<int:pk>/comment', PostCommentCreateView.as_view() , name = 'post-comment' ),
    path('video/<int:pk>/comment', VideoCommentCreateView.as_view() , name = 'video-comment' ),
    path('profile-pdf/', ProfilepdfView.as_view() , name = 'profile-pdf' ),
    path('q/', usersearch, name='search-user'),


    ]





