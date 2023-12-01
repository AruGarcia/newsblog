import pytest
from django.urls import reverse

from newspaper.django_assetions import assert_contains


@pytest.fixture
def resp_home(client):
    resp = client.get(reverse('base:home'))
    return resp


@pytest.fixture
def resp_about(client):
    resp = client.get(reverse('inst:about'))
    return resp


def test_status_code(resp_home):
    assert resp_home.status_code == 200


def test_title(resp_home):
    assert_contains(resp_home, '<title>NewsBlog - Home</title>')


def test_home_link(resp_home):
    assert_contains(resp_home, f'href="{reverse("base:home")}" class="logo m-0 float-start">NewsBlog')


def test_about_link(resp_about):
    assert_contains(resp_about, f'href="{reverse("inst:about")}">About</a>')
