from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import *
from .forms import *

from .key_generator import *

from datetime import date

def index(request):
    wtfs = WTF.objects.filter(created_timestamp__date=date.today())

    context = {
        'wtfs': wtfs,
    }

    template = loader.get_template('wtf/index.html')
    return HttpResponse(template.render(context, request))

def add_wtf(request):
    if request.method == 'POST':
        form = AddWTFForm(request.POST)
        if form.is_valid():
            wtf = WTF()
            wtf.content = form.cleaned_data.get('wtf_content')
            wtf.short = generate_key()

            wtf.save()

            return redirect(index)
    else:
        form = AddWTFForm()
    return render(request, 'wtf/add_wtf.html', {'form': form})

#def view_day(request, date):

#dev view_single(request, id)
