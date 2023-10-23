from venv import logger
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date

from django.urls import reverse
from django.views import View, generic
from django.contrib.auth import logout, authenticate, login

from .models import Course, User


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

def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return redirect('popular_course_list')

def login_request(request):
    context = {}
    # Handles POST request
    if request.method == "POST":
        # Get username and password from request.POST dictionary
        username = request.POST['username']
        password = request.POST['psw']
        # Try to check if provide credential can be authenticated
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is valid, call login method to login current user
            login(request, user)
            return redirect('popular_course_list')
        else:
            # If not, return to login page again
            return render(request, 'firstapp/user_login.html', context)
    else:
        return render(request, 'firstapp/user_login.html', context)
    
def registration_request(request):
    context = {}
    # If it is a GET request, just render the registration page
    if request.method == 'GET':
        return render(request, 'firstapp/user_registration.html', context)
    # If it is a POST request
    elif request.method == 'POST':
        # Get user information from request.POST
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            # Check if user already exists
            User.objects.get(username=username)
            user_exist = True
        except:
            # If not, simply log this is a new user
            logger.debug("{} is new user".format(username))
        # If it is a new user
        if not user_exist:
            # Create user in auth_user table
            user = User.objects.create(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            # Login the user and redirect to course list page
            login(request, user)
            return redirect("popular_course_list")
        else:
            return render(request, 'firstapp/user_registration.html', context)
