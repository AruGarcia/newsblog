import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from newspaper.blog.models import Post
from django.template.loader import render_to_string

from newspaper.django_assetions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('blog:blog'))
    return resp


@pytest.fixture
def user(db):
    UserModel = get_user_model()
    user = UserModel.objects.create_user(
        email='test@email.com',
        password='secret'
    )
    return user


@pytest.fixture
def post(user):
    return Post.objects.create(
        title='A good title',
        body='Nice body content',
        author=user,
    )


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_of_the_page(resp):
    assert_contains(resp, 'data-aos="fade-up">Blog</h1>')


def test_string_representation():
    post = Post(title='A sample title')
    assert str(post) == post.title


def test_post_content(post, user):
    assert str(post.title) == 'A good title'
    assert str(post.author.email) == user.email
    assert str(post.body) == 'Nice body content'


def test_post_template_content():
    posts = [
        {'title': 'Title 1', 'body': 'Body 1'},
        {'title': 'Title 2', 'body': 'Body 2'},
    ]

    rendered = render_to_string('blog/blog.html', {'all_posts_list': posts})

    assert all(item in rendered for item in ['Title 1', 'Body 1', 'Title 2', 'Body 2'])
