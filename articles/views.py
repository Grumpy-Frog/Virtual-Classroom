from braces.views import SelectRelatedMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from django.urls import reverse_lazy
from django.views import generic

from .models import Article
from classroom.models import Classroom, ClassMember


class CreateArticle(LoginRequiredMixin, generic.CreateView):
    model = Article
    fields = ("title", "description")

    def get_success_url(self):
        return reverse_lazy("classroom:single", kwargs={"slug": self.kwargs.get("slug")})

    def form_valid(self, form):
        code = self.kwargs.get("code")
        classroom = Classroom.objects.get(code=code)
        article_count = Article.objects.filter(classroom__code=code).count()
        if article_count >= 10:
            html = "<html><body><h1>Number of Articles reached its limit for this classroom</h1></body></html>"
            return HttpResponse(html)

        self.object = form.save(commit=False)
        self.object.creator = self.request.user


        self.object.classroom = classroom
        self.object.save()
        return super().form_valid(form)


class ArticleList(SelectRelatedMixin, generic.ListView):
    model = Article
    select_related = ("creator", "classroom")

    def get_queryset(self):
        queryset = super().get_queryset()
        classroom = Classroom.objects.get(slug=self.kwargs.get('slug'))
        return queryset.filter(classroom=classroom)


class DeleteArticle(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = Article
    select_related = ("creator", "classroom")

    def get_success_url(self):
        return reverse_lazy("Article:all", kwargs={"slug": self.kwargs.get("slug")})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Article Deleted")
        return super().delete(*args, **kwargs)


class UpdateArticle(LoginRequiredMixin, generic.UpdateView):
    model = Article


class ArticlePage(TemplateView):
    template_name = 'articles/article_showing_page.html'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['articles'] = Article.objects.all()
        context['classroom_code'] = self.request.GET.get('classroom_code')
        print(self.request.POST.get('classroom_code'))
        return context
