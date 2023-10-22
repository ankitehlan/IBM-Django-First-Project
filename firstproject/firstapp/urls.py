from django.urls import include, path
from . import views

urlpatterns = [
    path(route='', view=views.popular_course_list, name='popular_course_list'),
    path(route='date', view=views.get_date, name='date'),
    path(route='course/<int:course_id>/enroll/', view=views.enroll, name='enroll'),
    path(route='course/<int:course_id>', view=views.course_details, name='course_detail')
]
