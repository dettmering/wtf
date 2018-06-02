from django.http import HttpResponse, JsonResponse

from .models import *

from datetime import date

def today(request):
    wtfs = WTF.objects.filter(created_timestamp__date=date.today())

    data = {
        'count': len(wtfs),
    }

    return HttpResponse(JsonResponse(data), content_type="application/json")
