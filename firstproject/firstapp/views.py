from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


# Create your views here.
def index(request):
    template = "<html>This is my first django view create on html</html>"
    return HttpResponse(content=template)

def get_date(request):
    today = date.today()
    template = "<html>Today's date: {} </html>".format(today)
    return HttpResponse(content=template)