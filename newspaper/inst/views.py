from django.shortcuts import render


def about_page_view(request):
    return render(request, 'inst/about.html')
