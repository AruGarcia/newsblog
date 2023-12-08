from django.shortcuts import render

from newspaper.blog.models import Post


def blog_page_view(request):
    all_posts_list = Post.objects.all()
    context = {
        'all_posts_list': all_posts_list,
    }
    return render(request, 'blog/blog.html', context)


def blog_detail_view(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)
