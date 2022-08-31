from datetime import datetime, timedelta

import jwt
import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render
from feed.models import Post
from user_profile.models import Name

from .forms import ProfileUpdateForm, UserCreationForm, UserUpdateForm

LOGIN_API_URL = "http://127.0.0.2:8001/token"
CREATE_USER_URL = "http://127.0.0.2:8001/register"
USER_PROFILE_URL = "http://127.0.0.2:8001/users/"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        data = {
            "username": request.POST["username"],
            "email": request.POST["email"],
            "date_of_birth": request.POST["date_of_birth"],
            "password": request.POST["password1"],
        }
        login_info = {"username": data["username"], "password": data["password"]}
        if form.is_valid():
            if requests.post(CREATE_USER_URL, data=data).status_code == 201:
                user = authenticate(**login_info)
                response = requests.post(LOGIN_API_URL, data=login_info, timeout=5)
                login(request, user)
                if response.status_code == 200:
                    refresh, access = response.json().values()
                    token_info = jwt.decode(
                        access, key=settings.API_KEY, algorithms=["HS256"]
                    )
                    request.session["access"] = access
                    request.session["refresh"] = refresh
                    request.session["full_name"] = token_info.get("full_name")

                messages.success(
                    request, f"تهانينا {data['username']} لقد تمت عملية التسجيل بنجاح."
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
        # res = requests.get("http://127.0.0.2:8001/users/hello.world.2")
        if response.status_code == 200:
            refresh, access = response.json().values()
            token_info = jwt.decode(access, key=settings.API_KEY, algorithms=["HS256"])
            request.session["access"] = access
            request.session["refresh"] = refresh
            request.session["full_name"] = token_info.get("full_name")
            request.session["profile_imgs"] = token_info.get("profile_imgs")
            return redirect("home")
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
    posts = Post.objects.filter(user_id=request.user.id)
    user = requests.get(USER_PROFILE_URL + request.user.username, timeout=3).json()
    user["user_img"] = user["user_img"][0]
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
            "user_data": user,
            "posts": posts,
            "page": page,
            "post_list": post_list,
        },
    )


def profile_update(request):
    instance = Name.objects.get(user_id=request.user.id)
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=instance)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, "تم تحديث الملف الشخصي")
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=instance)

    context = {
        "title": "تعديل الملف الشخصي",
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, "user/profile_update.html", context)


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
