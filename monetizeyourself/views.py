from django.urls import reverse_lazy
from django.views.generic import TemplateView, \
    CreateView, UpdateView, DetailView, ListView

from monetizeyourself.forms import PostForm
from monetizeyourself.models import Post
from django.shortcuts import render


def index(request):
    context = {'form': PostForm()}
    return render(request, 'monetizeyourself/post_form.html', context)



class IndexView(TemplateView):
    # template_name = 'monetizeyourself/index.html'
    template_name = 'monetizeyourself/base.html'



class Index_2_View(TemplateView):
    template_name = 'monetizeyourself/index_2.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('monetizeyourself:post_list')

class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('monetizeyourself:post_list')
