# -*- coding: utf-8 -*-

from django.urls import path
from . import views
from landing.views import *


urlpatterns = [
    path('', views.index, name='indexpage'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
   
    path('gallary/', views.gallary, name='gallary'),
    path('contact/', ContactView.as_view(), name = 'contact'),
    path('subscription/', SubscribeView.as_view(), name = 'subscribe'),
    path('thinkaboutit/' , ThinkListView.as_view() , name = "think-list"),
  
    path('shareyourknowledge/', views.shareyourknowledge, name='shareyourknowledge'),
   
    path('privacy-policies/', views.policies, name='policy'),
    path('terms/', views.terms, name='terms'),
    path('community-guidelines/', views.community, name='community'),
    path('helpdesk/', views.helpdesk, name='helpdesk'),
    path('faq/', views.faq, name='faq'),
   
    
    
]

'''
business profile url -- 

 path('business-around-me/', businessprofileView.as_view(), name='business-list'),
    path('business-profile/new', businessprofileCreateView.as_view(), name='business-profile-create'),
    path('business-profile/<int:pk>', businessprofileDetailView.as_view(), name='business-detail'),
    path('business-profile/<int:pk>/update', businessprofileUpdateView.as_view(), name='business-profile-update'),
    path('business-profile/<int:pk>/delete', businessprofileDeleteView.as_view(), name='business-profile-delete'),

'''