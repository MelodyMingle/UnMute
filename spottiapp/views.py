from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm, CommentForm
from .models import Post, Comment
from django.urls import reverse_lazy
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id'] # this will order the posts by id in descending order
    ordering = ['-post_date']
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        get_likes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = get_likes.total_likes()
        context['total_likes'] = total_likes
        return context
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')
    # fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse_lazy('article-detail', args=[str(pk)]))
    # fields = ['title', 'title_tag', 'comment']
# def home(request):
#     return render(request, 'home.html', {})