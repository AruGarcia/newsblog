from django.urls import path

from newspaper.inst.views import about_page_view

app_name = "inst"
urlpatterns = [
    path('', about_page_view, name='about')
]
