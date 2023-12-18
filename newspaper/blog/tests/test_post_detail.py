import pytest

from django.urls import reverse


@pytest.fixture
def resp(client, create_post, db):
    post_id = create_post.id
    resp = client.get(reverse('blog:post_detail', kwargs={'pk': post_id}))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_post_content(create_post, db):
    post = create_post
    assert str(post.title) == 'A good title'
    assert str(post.author.email) == 'test@email.com'
    assert str(post.body) == 'Nice body content'
    assert post.category == 'Business'
    assert str(post.image) == 'post_images/images.jpg'


def test_post_content_in_template(resp, create_post, db):
    post = create_post
    assert post.title in str(resp.content)
    assert post.body in str(resp.content)
    assert post.category in str(resp.content)
    assert str(post.image) in str(resp.content)
