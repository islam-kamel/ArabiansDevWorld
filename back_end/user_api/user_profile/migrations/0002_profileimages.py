# Generated by Django 4.0.6 on 2022-08-22 13:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user_profile", "0001_initial"),
    ]

    operations = [
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
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_img",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
