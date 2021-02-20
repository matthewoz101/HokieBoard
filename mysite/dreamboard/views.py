from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import dream
from .forms import DreamForm

from . import urls

# Create your views here.


def index(request):

    if request.method == "GET":
        form = DreamForm()
        return render(request, 'dreamboard/index.html', {'form':form})
    else:
        form = DreamForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
