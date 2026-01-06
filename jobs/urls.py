from django.urls import path
from . import views

urlpatterns = [
    path('post_job/', views.job_post_view, name="post_job")
]