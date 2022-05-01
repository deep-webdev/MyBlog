import imp
from django.shortcuts import redirect, render
from blog.forms import PostForm, CommentClass
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from pytz import timezone
from blog.models import Post, Comments
# Create your views here.
#Use Django Generic Class Views

class AboutView(TemplateView):
    template_name = 'about.html'
    
class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    
class PostDetailView(DetailView):
    model = Post
    # template_name=''
    
class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    
    form_class = PostForm
    model = Post
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    
    form_class = PostForm
    model = Post
    
class PostDeleteview(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    
class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
