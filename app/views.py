from django.http import JsonResponse
from django.views import generic
from .forms import PostCreateForm
from .models import Post


class PostCreate(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = '/'


def api_posts_get(request):
    """サジェスト候補の記事をJSONで返す。"""
    keyword = request.GET.get('keyword')
    if keyword:
        post_list = [{'pk': post.pk, 'name': str(post)} for post in Post.objects.filter(title__icontains=keyword)]
    else:
        post_list = []
    return JsonResponse({'object_list': post_list})
