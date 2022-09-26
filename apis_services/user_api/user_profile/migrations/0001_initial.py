# Generated by Django 4.0.7 on 2022-09-26 00:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("country", models.CharField(max_length=50, verbose_name="Country")),
                ("city", models.CharField(max_length=50, verbose_name="City")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="address",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Bio",
            fields=[
                ("bio", models.TextField(max_length=255, verbose_name="Bio")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="bio",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GitHubAccount",
            fields=[
                ("github", models.CharField(max_length=50)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="github",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Name",
            fields=[
                (
                    "first_name",
                    models.CharField(max_length=50, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Last Name"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="name",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Phone",
            fields=[
                ("phone", models.CharField(max_length=15, verbose_name="Phone Number")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="phone",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProfileImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile_img",
                    models.ImageField(default="default.png", upload_to="profile_img"),
                ),
                ("cover_img", models.ImageField(upload_to="cover_img")),
            ],
        ),
        migrations.CreateModel(
            name="Skills",
            fields=[
                ("skill", models.CharField(max_length=150, unique=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="skills",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="skills",
            index=models.Index(
                fields=["user_id"], name="user_profil_user_id_ee1a3c_idx"
            ),
        ),
        migrations.AddField(
            model_name="profileimages",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_img",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddIndex(
            model_name="phone",
            index=models.Index(
                fields=["user_id"], name="user_profil_user_id_51841d_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="name",
            index=models.Index(
                fields=["user_id"], name="user_profil_user_id_22b8a4_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="githubaccount",
            index=models.Index(
                fields=["user_id"], name="user_profil_user_id_a2698b_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="bio",
            index=models.Index(
                fields=["user_id"], name="user_profil_user_id_6ba762_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="address",
            index=models.Index(
                fields=["user_id"], name="user_profil_user_id_00bb95_idx"
            ),
        ),
    ]
