from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('post_job/', views.job_post_view, name="post_job"),
    path('job_details/<int:pk>/',views.show_job_details, name="show_job_details")
]