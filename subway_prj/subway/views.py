from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.views.generic import View


def index(request):
    # return render(request, 'subway/test.html')
    return redirect('/map/')
    # return redirect('subway:map')


def map(request):
    return render(request, 'subway/map.html')

def detail(request):
    return render(request, 'subway/stationdetail.html')