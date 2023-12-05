import pytest
from django.urls import reverse

from newspaper.django_assetions import assert_contains


@pytest.fixture
def resp_home(client):
    resp = client.get(reverse('blog:blog'))
    return resp


def test_status_code(resp_home):
    assert resp_home.status_code == 200
