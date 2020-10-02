from django.db import models
from PIL import Image

class Question(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()

    class Meta:
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question


class Post(models.Model):
    text = models.CharField(max_length=300, null=True, blank=True)
    image = models.URLField(unique=True, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text

