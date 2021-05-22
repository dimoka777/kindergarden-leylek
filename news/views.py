from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm
from django.views.generic import TemplateView


class News(ListView):
    model = Post
    template_name = 'news/news.html'


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class BlogListView(ListView):
    model = Post
    template_name = 'index.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'news/post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_new.html'
    success_url = reverse_lazy('news')


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'news/post_edit.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('news')


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'news/post_delete.html'
    success_url = reverse_lazy('home')


