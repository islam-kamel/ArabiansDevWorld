from blog.models import Comment, Post
from django import template

register = template.Library()


@register.inclusion_tag("blog/latest_post.html")
def latest_posts():
    context = {
        "l_post": Post.objects.all()[0:5],
    }
    return context


@register.inclusion_tag("blog/latest_comments.html")
def latest_comments():
    context = {
        "l_comment": Comment.objects.filter(active=True)[:5],
    }

    return context


@register.filter(name="valid_url")
def valid_url(slug, pk):
    return f"{slug}-{pk}"
