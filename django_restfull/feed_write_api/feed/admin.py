from django.contrib import admin
from feed.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
