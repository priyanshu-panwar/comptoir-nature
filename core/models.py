from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()

    class Meta:
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question

