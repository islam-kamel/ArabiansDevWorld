import re

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, date_of_birth, password):
        if not email:
            raise ValueError(_("The Email must be set."))

        pattern = re.compile(
            r"^[a-zA](?=[a-zA-Z0-9._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$"
        )
        if not re.fullmatch(pattern, username):
            raise ValueError(_("Enter Valid Username"))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, date_of_birth, password):
        user = self.create_user(
            email=email,
            username=username,
            date_of_birth=date_of_birth,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    username = models.CharField(verbose_name="Username", max_length=50, unique=True)
    date_of_birth = models.DateField(verbose_name="Date of birth")
    join_date = models.DateTimeField(auto_now_add=timezone.now, editable=False)
    full_name = models.CharField(
        max_length=100, verbose_name="Full name", blank=True, null=True
    )
    bio = models.TextField(max_length=500, verbose_name="Bio", blank=True)
    skills = models.CharField(max_length=100, verbose_name="Your skills.", blank=True)
    phone = models.CharField(max_length=15, verbose_name="Phone Number", blank=True)
    github = models.CharField(
        max_length=150, verbose_name="Github username", blank=True
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "date_of_birth"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.is_admin

    def save(self, *args, **kwargs):
        if self.github != "":
            self.github = f"https://github.com/{self.github}"
        if self.skills:
            self.skills = self.skills.title()
        super(User, self).save(*args, **kwargs)
