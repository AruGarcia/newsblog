from django.urls import path

from newspaper.inst.views import about_page_view, contact_page_view

app_name = "inst"
urlpatterns = [
    path('about/', about_page_view, name='about'),
    path('contact/', contact_page_view, name='contact')
]
