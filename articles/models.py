from django.db import models
from classroom.models import Classroom
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="assignments")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="assignments")
    assign_time = models.DateTimeField(auto_now=True)


