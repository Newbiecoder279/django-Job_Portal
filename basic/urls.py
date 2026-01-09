from django.urls import path
from . import views

urlpatterns = [
   path('',views.home, name='home'),
   path('register/', views.registration, name='register'),
   path('login/', views.login, name='login'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('employer_dashboard/', views.dashboard, name='employer_dashboard'),
   path('search/', views.search, name='search' )

]