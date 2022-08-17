import requests
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView
from django.views.generic.edit import FormView
from feed.url_request import send_request

from .forms import PostCreateView, PostUpdateView
from .models import Post

read_post_url = "http://172.13.7.5:8000/feed/"


def landing_page(request):
    return render(request, "feed/landing_page.html")


def home(request):
    posts = send_request(read_post_url)
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
    return render(request, "feed/index.html", context)


def about(request):
    return render(request, "feed/about.html", {"title": "من نحن؟"})


def post_detail(request, slug):
    post = requests.get(read_post_url + slug).json()
    print(post)
    context = {
        "post": post,
    }
    return render(request, "feed/detail.html", context)


# class PostCreateView(FormView):
#     template_name = "feed/new_post.html"
#     form_class = PostCreateView
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, PostCreateView, FormView):
    model = Post
    template_name = "feed/new_post.html"
    form_class = PostCreateView

    # def get(self, request, *args, **kwargs):
    #     print(request.user)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "feed/post_update.html"
    form_class = PostUpdateView

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
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
