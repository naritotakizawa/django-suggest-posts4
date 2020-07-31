from django.contrib import admin
from .forms import PostCreateForm
from .models import Post


class PostAdmin(admin.ModelAdmin):
    form = PostCreateForm


admin.site.register(Post, PostAdmin)
