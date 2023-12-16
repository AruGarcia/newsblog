import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_status_code(client, create_post):
    post_id = create_post.id
    response = client.get(reverse('blog:post_detail', kwargs={'pk': post_id}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_content(create_post):
    post = create_post
    assert str(post.title) == 'A good title'
    assert str(post.author.email) == 'test@email.com'
    assert str(post.body) == 'Nice body content'
    assert post.category == 'Business'
    assert str(post.image) == 'post_images/images.jpg'


@pytest.mark.django_db
def test_post_content_in_template(client, create_post):
    post = create_post
    post_id = create_post.id
    response = client.get(reverse('blog:post_detail', kwargs={'pk': post_id}))
    assert post.title in str(response.content)
    assert post.body in str(response.content)
    assert post.category in str(response.content)
    assert str(post.image) in str(response.content)
