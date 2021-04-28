from datetime import timezone

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import *


def index(request):

    return render(request, "app_template/index.html")

class registerView(CreateView):
    form_class = SimpleUserForm
    success_url = reverse_lazy('app_html:index.html')
    template_name = 'registration/registration.html'

class GetCourseByID(DetailView):
    model = Courses
    template_name = "app_html/article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments_of_course'] = Comment.objects.filter(comment_on_course=self.object.id)
        crs_obj = self.get_object()
        crs_obj.save()
        return context

def leave_comment(request, id):
    if request.method == 'POST' and len(request.POST.get("comment_text")) > 0:
        print(request.POST.get("comment_text"), type(request.POST.get("comment_text")), type(request.user.id))
        comment_object = Comment(comment_text=request.POST.get("comment_text"),
                                      comment_on_course=Courses.objects.get(pk=id),
                                      comment_user=SimpleUser.objects.get(pk=request.user.id))
        comment_object.save()
        return redirect("app_html:get_course", pk=id)
    else:
        return render(request, "app_html/", {"empty_res": "There is no course"})

def rate_course(request, id):
    if request.method == 'POST':
        if request.POST.get("rate_val"):
            print(type(request.POST.get("rate_val")))
            course_obj = Courses.objects.get(pk=id)
            if course_obj.rating == 0.0:
                course_obj.rating = float(request.POST.get("rate_val"))
                course_obj.save()
            else:
                course_obj.rating = (course_obj.rating+float(request.POST.get("rate_val")))/2
                course_obj.save()
            return redirect("app_html:get_course", pk=id)
        else:
            return render(request, "app_html/search.html", {"empty_res": "There is no course"})