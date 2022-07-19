import requests
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView
from django.views.generic.edit import FormView

from .forms import PostCreateView, PostUpdateView
from .models import Post

read_post_url = "http://127.0.0.2:8001/feed/"


def landing_page(request):
    return render(request, "blog/landing_page.html")


def home(request):
    posts = requests.get(read_post_url).json()
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)
    context = {
        "title": "الصفحة الرئسية",
        "posts": posts,
        "page": page,
    }
    return render(request, "blog/index.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "من نحن؟"})


def post_detail(request, slug):
    post = requests.get(read_post_url + slug).json()
    context = {
        "post": post,
    }
    return render(request, "blog/detail.html", context)


class PostCreateView(FormView):
    template_name = "blog/new_post.html"
    form_class = PostCreateView

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     template_name = "blog/new_post.html"
#     form_class = PostCreateView
#
#     def get(self, request, *args, **kwargs):
#         print(request.user)
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    form_class = PostUpdateView

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
