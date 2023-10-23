from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date

from django.urls import reverse
from django.views import View, generic

from .models import Course


# Create your views here.
def index(request):
    template = "<html>This is my first django view create on html</html>"
    return HttpResponse(content=template)


def get_date(request):
    today = date.today()
    template = "<html>Today's date: {} </html>".format(today)
    return HttpResponse(content=template)


class CourseListView(View):
    def get(self, request):
        context = {}
        course_list = Course.objects.order_by("-total_enrollment")[:10]
        # Append the course list as an entry of context dict
        context["course_list"] = course_list
        return render(request, "firstapp/course_list.html", context)


def enroll(request, course_id):
    # If request method is POST
    if request.method == "POST":
        # First try to read the course object
        # If could be found, raise a 404 exception
        course = get_object_or_404(Course, pk=course_id)
        # Increase the enrollment by 1
        course.total_enrollment += 1
        course.save()
        # Return a HTTP response redirecting user to course list view
        return HttpResponseRedirect(reverse(viewname="popular_course_list"))


class CourseDetailsView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        course_id = kwargs.get('pk')
        try:
            course = Course.objects.get(pk=course_id)
            context["course"] = course
            # Use render() method to generate HTML page by combining
            # template and context
            return render(request, "firstapp/course_detail.html", context)
        except Course.DoesNotExist:
            # If course does not exist, throw a Http404 error
            raise get_object_or_404("No course matches the given id.")
        
class GenericCourseDetailsView(generic.DetailView):
    model = Course
    template_name = 'firstapp/course_detail.html'
