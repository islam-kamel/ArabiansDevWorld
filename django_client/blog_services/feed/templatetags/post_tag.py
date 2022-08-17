from django import template
from feed.models import Post

register = template.Library()


@register.inclusion_tag("feed/latest_post.html")
def latest_posts():
    context = {
        "l_post": Post.objects.all()[0:5],
    }
    return context


@register.filter(name="valid_url")
def valid_url(slug, pk):
    return f"{slug}-{pk}"
