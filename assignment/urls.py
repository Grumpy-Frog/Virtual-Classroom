from django.urls import path

from . import views

app_name = 'assignment'

urlpatterns = [
    path('create/<code>/<slug>', views.CreateAssignment.as_view(), name="create"),
    path("delete/<slug>/<pk>", views.DeleteAssignment.as_view(), name="delete"),
    path("update/", views.UpdateAssignment.as_view(), name="update"),
    path('all/<slug>', views.AssignmentList.as_view(), name="all"),
    path('assignment/<slug>/<int:pk>', views.AssignmentDetail.as_view(), name="single"),
    path('submit/<slug>/<int:pk>', views.SubmitAssignment.as_view(), name="submit"),
    path('view_submission/<int:pk>', views.ViewAssignmentSubmissions.as_view(), name="view"),
]
