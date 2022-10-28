from braces.views import SelectRelatedMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic

from .models import Assignment, AssignmentSubmission
from classroom.models import Classroom, ClassMember


class CreateAssignment(LoginRequiredMixin, generic.CreateView):
    model = Assignment
    fields = ("title", "description", "due", "points")

    def get_success_url(self):
        return reverse_lazy("classroom:single", kwargs={"slug": self.kwargs.get("slug")})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        code = self.kwargs.get("code")
        classroom = Classroom.objects.get(code=code)
        self.object.classroom = classroom

        self.object.save()
        return super().form_valid(form)


class AssignmentList(SelectRelatedMixin, generic.ListView):
    model = Assignment
    select_related = ("creator", "classroom")

    def get_queryset(self):
        queryset = super().get_queryset()
        classroom = Classroom.objects.get(slug=self.kwargs.get('slug'))
        return queryset.filter(classroom=classroom)


class DeleteAssignment(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = Assignment
    select_related = ("creator", "classroom")

    def get_success_url(self):
        return reverse_lazy("assignment:all", kwargs={"slug": self.kwargs.get("slug")})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Assignment Deleted")
        return super().delete(*args, **kwargs)


class UpdateAssignment(LoginRequiredMixin, generic.UpdateView):
    model = Assignment


class AssignmentDetail(LoginRequiredMixin, generic.DetailView):
    model = Assignment

    def get_context_data(self, **kwargs):
        classroom = Classroom.objects.get(slug=self.kwargs.get('slug'))
        assignment = Assignment.objects.get(pk=self.kwargs.get('pk'))
        student = self.request.user
        context = super().get_context_data(**kwargs)
        submitted = AssignmentSubmission.objects.filter(classroom=classroom, assignment=assignment,
                                                        student=student).exists()
        context["user_submitted"] = submitted
        class_member = ClassMember.objects.get(user=self.request.user, classroom=classroom)
        user_role = class_member.role
        context["user_role_in_classroom"] = user_role
        print(submitted)
        return context


class SubmitAssignment(LoginRequiredMixin, generic.CreateView):
    model = AssignmentSubmission
    fields = ('file',)
    template_name = "assignment/assignment_submission_form.html"

    def get_success_url(self):
        return reverse_lazy("classroom:single", kwargs={"slug": self.kwargs.get("slug")})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.student = self.request.user
        slug = self.kwargs.get("slug")
        classroom = Classroom.objects.get(slug=slug)
        self.object.classroom = classroom
        assignment_id = self.kwargs.get("pk")
        assignment = Assignment.objects.get(pk=assignment_id)
        self.object.assignment = assignment
        self.object.save()
        return super().form_valid(form)


class ViewAssignmentSubmissions(LoginRequiredMixin, SelectRelatedMixin, generic.ListView):
    model = AssignmentSubmission
    context_object_name = "submission_list"
    select_related = ('student', 'classroom', 'assignment')
    template_name = "assignment/assignment_submission_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        assignment_id = self.kwargs.get("pk")
        assignment = Assignment.objects.get(pk=assignment_id)
        return queryset.filter(assignment=assignment)


class Unsubmit(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = AssignmentSubmission
    select_related = ("student", "classroom", 'assignment')

    def get_success_url(self):
        return reverse_lazy("assignment:single", kwargs={"slug": self.kwargs.get("slug"), "pk": self.kwargs.get("pk")})

    def get_object(self, queryset=None):
        classroom = Classroom.objects.get(slug=self.kwargs.get("slug"))
        assignment = Assignment.objects.get(pk=self.kwargs.get("pk"))
        queryset = self.get_queryset()
        queryset = AssignmentSubmission.objects.get(classroom=classroom, assignment=assignment,
                                                    student=self.request.user)
        return queryset

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Unsubmitted. Don't forget to turn in your assignment")
        return super().delete(*args, **kwargs)
