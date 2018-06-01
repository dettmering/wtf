from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import *

def index(request):
    context = { }
    template = loader.get_template('wtf/index.html')
    return HttpResponse(template.render(context, request))

#def add_wtf(request):

#def view_day(request, date):

#dev view_single(request, id)
