from django.contrib import admin
from django.urls import path
from . import views

app_name="blog_app"

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('home/', views.blog_home, name='blog_home'),
    path('<int:blog_id>/', views.blog_details, name='blog_details')
]   
