from django.http import HttpResponse, JsonResponse
from django.template import loader

#from .models import StockItem, Pantry

def index(request):
    context = { }
    template = loader.get_template('wtf/index.html')
    return HttpResponse(template.render(context, request))
