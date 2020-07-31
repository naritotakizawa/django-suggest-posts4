from django import forms
from django.urls import reverse_lazy
from .models import Post
from .widgets import SuggestWidget


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': SuggestWidget(attrs={'data-url': reverse_lazy('app:api_posts_get')}),
        }
