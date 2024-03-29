from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from user.models import User

STATUS_CHOICES = (
    ("draft", "Draft"),
    ("published", "Published"),
)


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title", null=False)
    content = models.TextField(verbose_name="content", null=False)
    published_at = models.DateTimeField(auto_now_add=timezone.now)
    update_at = models.DateTimeField(auto_now=timezone.now)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="published")
    slug = models.SlugField(null=False, allow_unicode=True)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)

    class Meta:
        ordering = ("-published_at",)
        indexes = [
            models.Index(fields=["id"]),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("newsfeed:post_details", args=[self.slug, self.pk])

    def get_total_comments(self):
        total = Comment.objects.filter(post_id=self.id).count()  # noqa: F821
        return total

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)
