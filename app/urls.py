from django.urls import path
from django.contrib.auth.views import auth_login

from . import views
from .views import registerView, AllCourses, GetCourseByID, my_courses, ProfileView

urlpatterns = [
    path('', views.index, name='index'),
    path("register/", registerView.as_view(), name="registration"),
    path('', auth_login, name="login"),
    path('all_course/',AllCourses.as_view(),name="allCourses"),
    path('aboutUs',name="About Us"),
    path("course/id",GetCourseByID,name="courseID"),
    path("contatctUs", name="ContactUs"),
    path("my_curses/", my_courses, name="my_curses"),
    path("userPage",ProfileView,name="userPage"),
    path("id/coursePage",name="CoursePage")
]