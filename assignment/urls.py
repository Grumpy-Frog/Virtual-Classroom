from django.urls import path

from . import views

app_name = 'assignment'

urlpatterns = [
    # path('', views.ListClassrooms.as_view(), name="all"),
    path('create/', views.CreateAssignment.as_view(), name="create"),

]
