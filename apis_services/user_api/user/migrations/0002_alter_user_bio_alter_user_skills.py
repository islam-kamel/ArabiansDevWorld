# Generated by Django 4.0.7 on 2022-09-13 05:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="bio",
            field=models.TextField(blank=True, verbose_name="Bio"),
        ),
        migrations.AlterField(
            model_name="user",
            name="skills",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
