from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Post


class PostIndex(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post
