import pytest
from django.contrib.auth import get_user_model
from newspaper.blog.models import Post
from django.test import override_settings


@pytest.fixture
def create_user(db):

    return get_user_model().objects.create_user(
        email='test@email.com',
        password='secret',
    )


@pytest.fixture
def create_post(db, create_user):
    with override_settings(MEDIA_ROOT='/static/'):
        post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=create_user,
            category='Business',
            image='post_images/images.jpg',
        )
    return post
