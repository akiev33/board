from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic


from board_body.models import Post
from .forms import PostForm


def index(request):
    posts = Post.objects.all
    return render(request, 'index.html', locals())


class PostListView(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_crud/post_detail.html'
    context_object_name = 'post'
    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy('detail', kwargs={
            'pk': post_id})


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_crud/create.html'
    success_url = reverse_lazy('index')



class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_crud/update.html'
    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy('detail', kwargs={
            'pk': post_id})



class PostDeleteView(generic.DeleteView):
    model = Post
    form_class = PostForm
    template_name = 'post_crud/delete.html'
    success_url = reverse_lazy('index')

