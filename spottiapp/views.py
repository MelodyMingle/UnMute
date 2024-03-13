from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
from .models import Post
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id'] # this will order the posts by id in descending order 
    ordering = ['post_date'] 

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'



class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'



class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


    # fields = ['title', 'title_tag', 'comment']
    






# def home(request):
#     return render(request, 'home.html', {})