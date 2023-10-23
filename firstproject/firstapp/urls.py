from django.urls import include, path
from . import views

urlpatterns = [
    path(route='', view=views.CourseListView.as_view(), name='popular_course_list'),
    path(route='date', view=views.get_date, name='date'),
    path(route='course/<int:course_id>/enroll/', view=views.enroll, name='enroll'),
    path(route='course/<int:pk>', view=views.CourseDetailsView.as_view(), name='course_detail'),
    path(route='course/<int:pk>', view=views.GenericCourseDetailsView.as_view(), name='generic_course_detail')
]
