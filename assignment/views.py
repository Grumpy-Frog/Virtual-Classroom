from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import generic

from .models import Assignment


class CreateAssignment(LoginRequiredMixin, generic.CreateView):
    model = Assignment
    fields = ("title", "description", "due", "points")
