import re

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from user.models import User


class UserCreationFrom(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("full_name", "username", "email", "date_of_birth", "is_active")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        is_valid = re.search(
            r"^[a-zA](?=[a-zA-Z0-9._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$",
            username,
        )
        if not is_valid:
            raise ValidationError("Enter Valid Username")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            "full_name",
            "username",
            "email",
            "password",
            "date_of_birth",
            "bio",
            "github",
            "phone",
            "skills",
            "is_active",
            "is_admin",
        )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        is_valid = re.search(
            r"^[a-zA](?=[a-zA-Z0-9._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$",
            username,
        )
        if not is_valid:
            raise ValidationError("Enter Valid Username")
        return username


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationFrom

    readonly_fields = ("join_date",)
    list_display = ("username", "email", "is_admin")
    list_filter = ("is_admin",)
    fieldsets = (
        (None, {"fields": ("username", "join_date", "password")}),
        (
            "Personal info",
            {"fields": ("bio", "full_name", "github", "skills", "date_of_birth")},
        ),
        ("Contact info", {"fields": ("phone", "email")}),
        (
            "Permissions",
            {
                "fields": ("is_active", "is_admin"),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "full_name",
                    "username",
                    "email",
                    "bio",
                    "date_of_birth",
                    "github",
                    "phone",
                    "skills",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    search_fields = ("email", "username")
    ordering = ("join_date",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
