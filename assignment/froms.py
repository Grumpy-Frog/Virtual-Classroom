from django import forms
from . import models


class AssignmentForm(forms.ModelForm):
    class Meta:
        fields = ("title", "description", "due", "points")
        model = models.Assignment
