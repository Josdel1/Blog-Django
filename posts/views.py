from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from .forms import PostForm

class PostListView(generic.ListView):
    template_name = 'index.html'
    model = Post
    
class PostCreateView(generic.CreateView):
    template_name = 'createpost.html'
    form_class = PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context

class PostDetailView(generic.DetailView):
    template_name = 'posts.html'
    model = Post