from django.utils import timezone

from django.urls import reverse

from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('Business', 'Business'),
        ('Culture', 'Culture'),
        ('Food', 'Food'),
    ]

    title = models.CharField(max_length=200)
    body = models.TextField(default=None)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Business',

    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
