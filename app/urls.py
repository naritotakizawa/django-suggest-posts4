from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.PostCreate.as_view(), name='create'),
    path('api/posts/get/', views.api_posts_get, name='api_posts_get')
]
