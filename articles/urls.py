from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    path('create/<code>/<slug>', views.CreateArticle.as_view(), name="create"),
    path("delete/<slug>/<pk>", views.DeleteArticle.as_view(), name="delete"),
    path("update/", views.UpdateArticle.as_view(), name="update"),
    path('all/<slug>', views.ArticleList.as_view(), name="all"),
    path('articles/<code>/<slug>', views.ArticlePage.as_view(), name='articles')
]