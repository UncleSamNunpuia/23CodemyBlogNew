from django.shortcuts import render

# added below
from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from . import models as md
from django.urls import reverse
from .forms import PostForm
# Create your views here.


def homePage(request):
    return render(request, 'blogHomePage.html', {'page_title': 'website home page'})


class HomeView(ListView):
    model = md.Post
    template_name = 'home.html'

    # this makes var my_variable accessible on html page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Home of Blog Section'
        # context['my_vars'] = 'nunpuia dinfela'
        return context


class ArticleView(DetailView):
    model = md.Post
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Article page of Blog Section'
        return context


class AddPost(CreateView):
    model = md.Post
    form_class = PostForm
    template_name = 'addPost.html'
    # below added to use our form from forms.y tehn fields ill have to be removed
    # this adds all fields
    # fields = '__all__'
    # tis adds selectted fields
    # fields = ('post_title', 'author', 'post_content')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'AddPage section of Blog'
        # context['my_vars'] = 'nunpuia dinfela'
        return context


class UpdatePost(UpdateView):
    model = md.Post
    # form_class = PostForm
    template_name = 'updatePost.html'
    # below added to use our form from forms.y tehn fields ill have to be removed
    # this adds all fields
    # fields = '__all__'
    # tis adds selectted fields
    fields = ('post_title', 'author', 'post_content', 'image')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'AddPage section of Blog'
        # context['my_vars'] = 'nunpuia dinfela'
        return context
