from datetime import datetime, timedelta

import jwt
import requests
from blog.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from .forms import UserCreationForm

LOGIN_API_URL = "http://127.0.0.2:8001/token"
SECRET_KEY = "django-insecure-l2mx!ysmhtsq2%hl09ty(=6bc_&a!xo!uv^-v%nkx-ou=(*i)8"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password1"])
            new_user.save()
            messages.success(
                request, f"تهانينا {new_user} لقد تمت عملية التسجيل بنجاح."
            )
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(
        request,
        "user/register.html",
        {
            "title": "التسجيل",
            "form": form,
        },
    )


def login_user(request):
    if request.method == "POST":
        data = {
            "username": request.POST["username"],
            "password": request.POST["password"],
        }
        user = authenticate(**data)
        login(request, user)
        response = requests.post(LOGIN_API_URL, data=data, timeout=5)
        if response.status_code == 200:
            refresh, access = response.json().values()
            token_info = jwt.decode(access, key=SECRET_KEY, algorithms=["HS256"])
            request.session["access"] = access
            request.session["refresh"] = refresh
            request.session["full_name"] = token_info.get("full_name")
            response = redirect("home")
            return response
        else:
            messages.warning(request, "أسم المستخدم أو كلمة المرور خطاء")

    return render(
        request,
        "user/login.html",
        {
            "title": "تسجيل الدخول",
        },
    )


def logout_user(request):
    logout(request)
    return render(request, "user/logout.html", {"title": "تسجيل الخروج"})


@login_required(login_url="login")
def profile(request):
    posts = Post.objects.filter(author=request.user)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_page)

    return render(
        request,
        "user/profile.html",
        {
            "title": "الملف الشخصي",
            "posts": posts,
            "page": page,
            "post_list": post_list,
        },
    )


#
# def profile_update(request):
#     if request.method == "POST":
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         profile_form = ProfileUpdateForm(
#             request.POST, request.FILES, instance=request.user.profile
#         )
#         if user_form.is_valid and profile_form.is_valid:
#             user_form.save()
#             profile_form.save()
#             messages.success(request, "تم تحديث الملف الشخصي")
#             return redirect("profile")
#     else:
#         user_form = UserUpdateForm(instance=request.user)
#         profile_form = ProfileUpdateForm(instance=request.user.profile)
#
#     context = {
#         "title": "تعديل الملف الشخصي",
#         "user_form": user_form,
#         "profile_form": profile_form,
#     }
#     return render(request, "user/profile_update.html", context)


def set_cookie(response, name: str, access, exp):
    return response.set_cookie(
        key=name,
        value=access,
        httponly=True,
        samesite="lax",
        secure=True,
        expires=datetime.strftime(
            datetime.utcnow() + timedelta(milliseconds=exp), "%a, %d-%b-%Y %H:%M:%S GMT"
        ),
    )
