from django.urls import path
from django.contrib.auth.views import auth_login

from . import views
from .views import registerView

urlpatterns = [
    path('', views.index, name='index'),
    path("register/", registerView.as_view(), name="registration"),
    path('', auth_login, name="login"),
]