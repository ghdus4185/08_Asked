from django.db import models

# Create your models here.

# 모델을 바꾸면 migrations


class Question(models.Model):
    content = models.TextField()


class Answer(models.Model):
    content = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
