from django import forms
from .models import Assignment


class AssignmentForm(forms.ModelForm):
    class Meta:
        fields = ("title", "description", "due", "points")
        model = Assignment
