from django.urls import path

from newspaper.blog.views import blog_page_view, blog_detail_view, blog_create_view

app_name = "blog"
urlpatterns = [
    path('blog/post/<int:pk>/', blog_detail_view, name='post_detail'),
    path('blog/post/new/', blog_create_view, name='post_new'),
    path('blog/', blog_page_view, name='blog'),
]
