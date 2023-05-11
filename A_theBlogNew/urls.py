"""P_codemyBlogNew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # below are urls mainly for the Blog
    # path('admin/', admin.site.urls),
    path('', views.homePage, name='websiteHome'),
    path('blog/', views.HomeView.as_view(), name='blog_homePage'),
    path('article/<int:pk>', views.ArticleView.as_view(), name='blog_article'),
    path('blog/add_post', views.AddPost.as_view(), name='blog_addPost'),
    path('blog/update_post/<int:pk>',
         views.UpdatePost.as_view(), name='blog_updatePost'),
    #  below urls are mainly for KTPinkhawmProg
    # path('', views.homePage, name='websiteHome'),

]
