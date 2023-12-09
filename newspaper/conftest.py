import pytest
from django.contrib.auth import get_user_model
from newspaper.blog.models import Post


@pytest.fixture
def create_post(db):
    post = Post.objects.create(
        title='A good title',
        body='Nice body content',
        author=get_user_model().objects.create_user(
            email='test@email.com',
            password='secret'
        ),
    )
    return post
