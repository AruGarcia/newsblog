from django.urls import path

from newspaper.blog.views import blog_page_view

app_name = "blog"
urlpatterns = [
    path('blog/', blog_page_view, name='blog')
]
