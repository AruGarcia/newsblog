from django.shortcuts import render


def blog_page_view(request):
    return render(request, 'blog/blog.html')
