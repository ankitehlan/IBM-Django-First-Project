from django.urls import include, path
from . import views

urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='date', view=views.get_date, name='date')
]
