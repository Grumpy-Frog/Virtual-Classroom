from django.db import models
from classroom.models import Classroom


# Create your models here.

class Assignment(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    assign_time = models.DateTimeField(auto_now=True)
    due = models.DateTimeField()
    points = models.IntegerField()
