from django.urls import include, path
from . import views

urlpatterns = [
    path(route='', view=views.CourseListView.as_view(), name='popular_course_list'),
    path(route='date', view=views.get_date, name='date'),
    path(route='course/<int:course_id>/enroll/', view=views.enroll, name='enroll'),
    path(route='course/<int:pk>', view=views.CourseDetailsView.as_view(), name='course_detail'),
    path(route='course/<int:pk>', view=views.GenericCourseDetailsView.as_view(), name='generic_course_detail'),
    path('login/', views.login_request, name='login'),
    path(route='logout/', view=views.logout_request, name='logout'),
    path(route='registration/', view=views.registration_request, name='registration')
]
