import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from feed.url_request import submit_request

from .forms import PostCreateForm, PostUpdateForm
from .models import Post

read_create_post_url = "http://127.0.0.3:8002/feed/"


def landing_page(request):
    return render(request, "feed/landing_page.html")


def home(request):
    posts = submit_request(read_create_post_url, method="GET").json()
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    print(request.user)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        "title": "الصفحة الرئسية",
        "posts": posts,
        "page": page,
    }
    return render(request, "feed/index.html", context)


def about(request):
    return render(request, "feed/about.html", {"title": "من نحن؟"})


class PostDetailsView(View):
    def get(self, request, slug):
        post = requests.get(read_create_post_url + slug).json()
        context = {
            "post": post,
        }
        return render(request, "feed/detail.html", context)


@method_decorator(login_required(login_url="login"), name="dispatch")
class PostCreateView(View):
    form = PostCreateForm

    def get(self, request):
        return render(request, "feed/new_post.html", {"form": self.form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.cleaned_data["user_id"] = request.user.id
            response = submit_request(
                url=read_create_post_url,
                data=form.cleaned_data,
                token=request.session["access"],
            )
            if response.status_code == 201:
                messages.success(request, "رائع انشاءت منشور للتو 🎊")
                return redirect("home")
        return render(request, "feed/new_post.html", {"form": form})


@method_decorator(login_required(login_url="login"), name="dispatch")
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get_object(self, slug):
        obj = submit_request(read_create_post_url + slug, method="GET")
        return obj.json()

    def get(self, request, slug):
        obj = self.get_object(slug)
        form = PostUpdateForm(data=obj)
        context = {"form": form}
        return render(request, "feed/post_update.html", context)

    def post(self, request, slug):
        obj = self.get_object(slug)
        form = PostUpdateForm(data=request.POST)
        if self.is_owner(request, obj) and form.is_valid():
            response = submit_request(
                read_create_post_url + slug,
                data=form.cleaned_data,
                token=request.session["access"],
            )
            return redirect("detail", slug=slug)

    def is_owner(self, request, obj=None):
        if obj["user_id"] == request.user.id:
            return True
        return False

    def test_func(self, **kwargs):
        obj = self.get_object(self.kwargs["slug"])
        if obj["user_id"] == self.request.user.id:
            return True
        return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, View):
    model = Post
    success_url = "/"

    obj = None

    def get_object(self, slug):
        obj = submit_request(read_create_post_url + slug, method="GET")
        return obj.json()

    def get(self, request, slug):
        res = submit_request(
            read_create_post_url + slug,
            method="DELETE",
            token=self.request.session["access"],
        )
        if res.status_code == 204:
            return redirect("home")

    def test_func(self):
        self.obj = self.get_object(self.kwargs["slug"])
        if self.obj["user_id"] == self.request.user.id:
            return True
        return False
