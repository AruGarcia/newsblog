import pytest
from django.urls import reverse

from newspaper.django_assetions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>NewsBlog - Home</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}" class="logo m-0 float-start">NewsBlog')
