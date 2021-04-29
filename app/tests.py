from django.test import TestCase
from .models import *

# Create your tests here.
class SimpleUserTest(TestCase):
    def test_get_name(self):
        simpleUser = SimpleUser(username="John")
        self.assertTrue(simpleUser.get_name()=="John", "get_name() method testing failed")

class CourseRatingTests(TestCase):
    def setUp(self):
        Courses.objects.create(id=1001,
                               course_name="Test course name",
                               course_description="Test course description",
                               course_date="24.07.2021",
                               counter_rating=4,
                               sum_rating=3.5,
                               course_requirements="Test course req",)

    def test_course_rating_more_than_three(self):
        course = Courses.objects.get(pk=1001)
        self.assertTrue(course.get_rating()>3, "Less than 3")


    def test_set_new_rating(self):
        course = Courses.objects.get(pk=1001)
        course.rating=5
        self.assertEqual(course.get_rating(), 5, "Setting new value failed")
