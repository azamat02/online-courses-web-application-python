from datetime import timezone

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from .forms import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view # making sure to receive Request, add context to Response
from rest_framework.response import Response # is needed to return client defined response

def index(request):
    return render(request, "app/index.html")

class registerView(CreateView):
    form_class = SimpleUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'

class GetCourseByID(DetailView):
    model = Courses
    template_name = "app/course.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments_of_course'] = Comment.objects.filter(comment_on_course=self.object.id)
        crs_obj = self.get_object()
        crs_obj.save()
        return context

class AllCourses(ListView):
    template_name = 'app/all_course.html'
    context_object_name = 'all_course'
    queryset = Courses.objects.order_by('course_name')


def my_courses(request):
    result = Purchased_Courses.objects.filter(pc_user=request.user.id)
    return render(request, "app/my_courses.html",
                  {"result": result, "empty_result": "There is no courses"})


def purchase_courses(request, id):
    if request.method == 'POST':
        purchase_object = Purchased_Courses(pc_date=timezone.now(),
                                            pc_user=request.user.id,
                                            pc_course=id)
        purchase_object.save()
        return redirect("app:home")

def leave_comment(request, id):
    if request.method == 'POST' and len(request.POST.get("comment_text")) > 0:
        print(request.POST.get("comment_text"), type(request.POST.get("comment_text")), type(request.user.id))
        comment_object = Comment(comment_text=request.POST.get("comment_text"),
                                      comment_on_course=Courses.objects.get(pk=id),
                                      comment_user=SimpleUser.objects.get(pk=request.user.id))
        comment_object.save()
        return redirect("app:get_course", pk=id)
    else:
        return render(request, "app/search.html", {"empty_res": "There is no course"})

def rate_course(request, id):
    if request.method == 'POST':
        if request.POST.get("rate_val"):
            print(type(request.POST.get("rate_val")))
            course_obj = Courses.objects.get(pk=id)
            course_obj.sum_rating = course_obj.sum_rating + float(request.POST.get("rate_val"))
            course_obj.counter_rating = course_obj.counter_rating + 1;
            course_obj.save()
            return redirect("app:get_course", pk=id)
        else:
            return render(request, "app/search.html", {"empty_res": "There is no course"})

class ContactsView(TemplateView):
    template_name = "app/contacts.html"

class AboutView(TemplateView):
    template_name = "app/about.html"

class ProfileView(TemplateView):
    template_name = "registration/user_page.html"

class ChangeView(TemplateView):
    template_name = "register/change_userserializers.py.html"

def search_by_course_text(request):
    if request.method == "POST" and len(request.POST.get("search_field")) > 0:
        searching_text = request.POST.get("search_field")
        return redirect("app:search_success", text=searching_text)
    else:
        return render(request, "app/search.html",
                      {"empty_res": "There is no article"})

def search_success(request, text):
    if len(text) > 0:
        search_res = Courses.objects.filter(course_name_contains=text)
        return render(request, "app/search.html",
                      {"search_res": search_res, "empty_res": "There is no article"})