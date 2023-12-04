import pytest
from django.urls import reverse

from newspaper.django_assetions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('inst:contact'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>NewsBlog - Contact Us</title>')


def test_location_information(resp):
    assert_contains(resp, '<p>43 Raymouth Rd. Baltemoer,<br> London 3910</p>')


def test_open_hours_information(resp):
    days_of_week = 'Sunday-Friday'
    hours = '11:00 AM - 23:00 PM'

    assert_contains(resp, f'{days_of_week}:')
    assert_contains(resp, f'{hours}')


def test_contact_email(resp):
    email = 'foo@bar.com'
    assert_contains(resp, f'{email}')


def test_contact_number(resp):
    phone = '+1 1234 55488 55'
    assert_contains(resp, f'{phone}')
