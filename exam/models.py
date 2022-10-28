from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Exam(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_marks = models.IntegerField()


class ExamQuestion(models.Model):
    description = models.CharField(max_length=50)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    option1 = models.CharField(max_length=10)
    option2 = models.CharField(max_length=10)
    option3 = models.CharField(max_length=10)
    option4 = models.CharField(max_length=10)
    Answer = models.IntegerField()