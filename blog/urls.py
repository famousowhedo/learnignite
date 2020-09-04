from django.urls import path
from .views import  CourseListView, CourseDetailView , CourseCreateView
from .import views


urlpatterns = [
    path('',CourseListView.as_view(), name='home'),
    path('post/<int:pk>/',CourseDetailView.as_view(), name='post-detail'),
    path('post/new/',CourseCreateView.as_view(), name='post-create'),
]
