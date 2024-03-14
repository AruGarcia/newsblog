import pytest
from django.urls import reverse
from model_bakery import baker
from forms import YourPostForm
from newspaper.django_assetions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('blog:post_new'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_of_the_page(resp):
    assert_contains(resp, 'data-aos="fade-up">New Post</h1>')


# def test_create_valid_post(db):
#     post = baker.make('blog.Post', body='Post body content')
#
#     assert post.pk is not None
#
#
# def test_create_post_with_invalid_data(db):
#     with pytest.raises(ValueError):
#         # Test creating a post with missing required fields
#         baker.make('blog.Post', title='', body='Some body content')
#
#     # Test creating a post with other invalid data scenarios...
#     # For instance, testing constraints or data formats
#
#     with pytest.raises(ValueError):
#         # Test creating a post with a null body
#         baker.make('blog.Post', body=None)


def test_post_creation(db):
    # Test creating a valid Post
    post = baker.make('blog.Post', body='Post body content')
    assert post.pk is not None


# def test_post_title_length_limit(db):
#     # Test title exceeding maximum length
#     with pytest.raises(ValueError) as excinfo:
#         baker.make('blog.Post', title='A' * 201, body='Post body content')
#
#     assert excinfo.value.args[0] == 'value too long for type character varying(200)'

def test_post_body_not_null(db):
    # Test that body cannot be null
    with pytest.raises(ValueError):
        baker.make('blog.Post', body=None)
