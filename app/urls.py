from django.urls import path
from django.contrib.auth.views import auth_login

from . import views
from .views import *

urlpatterns = [
    path('api/courses/all/', CoursesListAPI.as_view(), name='api-courses-list'),
    path('api/comments/all', CommentsListAPI.as_view(), name='api-comment-details'),
    path('api/comments/comment/<int:pk>/', CommentDetailsAPI.as_view(), name='api-comment-details'),
    path('', views.index, name='index'),
    path("register/", registerView.as_view(), name="registration"),
    path('', auth_login, name="login"),
    path('all_course/', AllCourses.as_view(), name="allCourses"),
    path('aboutUs', AboutView.as_view(), name="About Us"),
    path("course/id", GetCourseByID, name="courseID"),
    path("contatctUs", ContactsView.as_view(), name="ContactUs"),
    path("my_curses/", my_courses, name="my_curses"),
    path("user/<username>", ProfileView.as_view(), name="profile"),
]