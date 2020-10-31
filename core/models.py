from django.db import models
from PIL import Image
from django.utils import timezone

class Text(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    Section_1 = models.TextField()
    Section_2 = models.TextField()
    Section_3 = models.TextField()
    Section_4 = models.TextField()
    Section_5 = models.TextField()

    def __str__(self):
        return "DEFAULT"

class Question(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()

    class Meta:
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question


class Post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    image = models.URLField(max_length=500, unique=True, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    tag = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Publications"

    def __str__(self):
        return self.text

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contacts"
        ordering = ['-date',]

    def __str__(self):
        return self.email


class Utility(models.Model):
	hours = models.TextField()

	class Meta:
		verbose_name_plural = "Utilities"

	def __str__(self):
		return f"Default"
