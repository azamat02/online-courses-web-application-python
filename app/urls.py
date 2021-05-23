from django.urls import path
from django.contrib.auth.views import auth_login

from . import views
from .views import *

urlpatterns = [
    path('api/courses/all/', CoursesListAPI.as_view(), name='api-courses-list'),
    path('api/comments/all', CommentsListAPI.as_view(), name='api-comment-details'),
    path('api/comments/comment/<int:pk>/', CommentDetailsAPI.as_view(), name='api-comment-details'),
    path('', IndexView.as_view(), name='index'),
    path("register/", registerView.as_view(), name="registration"),
    path('', auth_login, name="login"),
    path('course/<int:id>/purchase', purchase_courses, name="purchase"),
    path('course/<int:pk>/', GetCourseByID.as_view(), name='get_course_by_id'),
    path('course/<int:id>/rate', rate_course, name='rate_course'),
    path('course/<int:id>/leaving_comment', leave_comment, name='leave_comment'),
    path('all_course/', AllCourses.as_view(), name="allCourses"),
    path('aboutUs', AboutView.as_view(), name="aboutUs"),
    path("course/id", GetCourseByID, name="courseID"),
    path("contactUs", ContactsView.as_view(), name="contactUs"),
    path("my_curses/", my_courses, name="my_curses"),
    path("user/<username>", ProfileView.as_view(), name="profile"),
]