from django.urls import include, path
from django.conf import settings
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blogs, name='all_blogs'),
    path('<int:blog_id>', views.detail, name='detail'),
]