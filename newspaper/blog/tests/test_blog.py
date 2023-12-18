import re

import pytest

from django.urls import reverse
from bs4 import BeautifulSoup
from newspaper.blog.models import Post
from django.template.loader import render_to_string

from newspaper.django_assetions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('blog:blog'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_of_the_page(resp):
    assert_contains(resp, 'data-aos="fade-up">Blog</h1>')


def test_string_representation():
    post = Post(title='A sample title')
    assert str(post) == post.title


def test_post_content(create_post):
    post = create_post
    assert str(post.title) == 'A good title'
    assert str(post.author.email) == 'test@email.com'
    assert str(post.body) == 'Nice body content'
    assert post.category == 'Business'
    assert str(post.image) == 'post_images/images.jpg'


def test_post_template_content():
    posts = [
        {'title': 'Title 1', 'body': 'Body 1', 'pk': 1},
        {'title': 'Title 2', 'body': 'Body 2', 'pk': 2},
    ]

    rendered = render_to_string('blog/blog.html', {'all_posts_list': posts})
    assert all(item in rendered for item in ['Title 1', 'Body 1', 'Title 2', 'Body 2'])


def test_conditional_element_when_no_image(resp, create_post):
    post_without_image = create_post
    post_without_image.image = None
    post_without_image.save()

    soup = BeautifulSoup(resp.content, 'html.parser')
    img_link_element = soup.find('a', class_='img-link')

    assert img_link_element is None


def test_conditional_element_when_image_present(client, create_post):
    response = client.get(reverse('blog:blog'))
    assert response.status_code == 200

    soup = BeautifulSoup(response.content, 'html.parser')
    img_link_element = soup.find('a', class_='img-link')

    assert img_link_element is not None


def test_img_element_with_src_and_alt(resp, create_post):
    assert resp.status_code == 200

    soup = BeautifulSoup(resp.content, 'html.parser')
    img_element = soup.find('img')

    assert img_element is not None
    assert 'src' in img_element.attrs
    assert 'alt' in img_element.attrs

    expected_src = '/static/images/img_1_sq.jpg'
    expected_alt = 'Image placeholder'

    assert img_element['src'] == expected_src
    assert img_element['alt'] == expected_alt


def test_date_format(client, create_post):
    response = client.get(reverse('blog:blog'))

    soup = BeautifulSoup(response.content, 'html.parser')
    date_elements = soup.find_all(class_='date')

    date_regex = (r'^\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.\s+(\d{1,2}),\s+(\d{4}),\s+(\d{1,'
                  r'2}):(\d{2})\s+([APap]\.m\.)\s*•')

    for element in date_elements:
        text = element.get_text()
        print("Element text:", text)

        date_match = re.search(date_regex, text)
        if date_match:
            print(date_match.group())
            assert True
            return

    assert False, "Formatted date not found"


def test_category_format(client, create_post):
    response = client.get(reverse('blog:blog'))

    soup = BeautifulSoup(response.content, 'html.parser')
    category_elements = soup.find_all('a')

    for element in category_elements:
        if element.parent.get('class') == ['date']:
            formatted_category = element.get_text()

            print("Formatted Category:", formatted_category)

            assert formatted_category
            return

    assert False, "Formatted category not found"


def test_href_is_generated_correctly(create_post, client):
    post = create_post

    response = client.get(reverse('blog:blog'))
    soup = BeautifulSoup(response.content, 'html.parser')
    post_detail_url = reverse('blog:post_detail', kwargs={'pk': post.pk})

    assert f'href="{post_detail_url}"' in str(soup)
