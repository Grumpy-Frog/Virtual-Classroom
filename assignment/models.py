from django.db import models
from classroom.models import Classroom
from django.contrib.auth.models import User

from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


# Create your models here.

class Assignment(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="assignments")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="assignments")
    assign_time = models.DateTimeField(auto_now=True)
    due = models.DateTimeField()
    points = models.IntegerField()


class AssignmentSubmission(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="submission")
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="submission")
    file = models.FileField(upload_to='media', storage=gd_storage)
    submission_time = models.DateTimeField(auto_now=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submission")
