from django.shortcuts import render
from django.views.generic import CreateView

from forms import YourPostForm
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


class BlogCreateView(CreateView):
    model = Post
    form_class = YourPostForm
    template_name = 'blog/post_new.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()
