from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    body = models.TextField(default='')

    def __str__(self):
        return self.title
