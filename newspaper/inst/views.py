from django.shortcuts import render


def about_page_view(request):
    return render(request, 'inst/about.html')


def contact_page_view(request):
    days_of_week = 'Sunday-Friday'
    hours = '11:00 AM - 23:00 PM'
    email = 'foo@bar.com'
    phone = '+1 1234 55488 55'

    context = {
        'days_of_week': days_of_week,
        'hours': hours,
        'email': email,
        'phone': phone,
    }

    return render(request, 'inst/contact.html', context)
