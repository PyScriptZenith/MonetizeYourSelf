from django.urls import reverse_lazy
from django.views.generic import TemplateView, \
    CreateView, UpdateView, DetailView

from monetizeyourself.forms import PostForm
from monetizeyourself.models import Post


class IndexView(TemplateView):
    template_name = 'monetizeyourself/index.html'



class Index_2_View(TemplateView):
    template_name = 'monetizeyourself/index_2.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('monetizeyourself:index')

class PostDetailView(DetailView):
    model = Post
