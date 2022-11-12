from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    path('create/<code>/<slug>/<name>', views.CreateArticle.as_view(), name="create"),
    path("delete/<slug>/<pk>", views.DeleteArticle.as_view(), name="delete"),

    path('all/<slug>', views.ArticleList.as_view(), name="all"),
    path('articles/<code>/<slug>/<name>', views.ArticlePage.as_view(), name='articles'),
    path('pending_articles/<code>/<slug>/<name>', views.PendingArticlePage.as_view(), name='pending_articles'),

    path('update/<slug>/<int:pk>', views.UpdateArticle.as_view(), name="update"),
    path('updaterecord/<int:pk>', views.UpdateRecord, name="update_record"),
]
