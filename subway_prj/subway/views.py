from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.views.generic import View, DetailView

from .models import Station, Congestion, Tourspot


def index(request):
    # return render(request, 'subway/test.html')
    return redirect('/map/')
    # return redirect('subway:map')


def map(request):
    return render(request, 'subway/map.html')

# def detail(request):
#     return render(request, 'subway/stationdetail.html')

class detail(DetailView) :
    template_name = 'subway/stationdetail.html'

    def get(self, request):

        current_time = datetime.now()
        nowtime = ''
        if current_time.strftime("%p") == 'AM':
            nowtime = '오전 {}:{}'.format(current_time.strftime("%I"), current_time.strftime("%M"))
        elif current_time.strftime("%p") == 'PM':
            nowtime = '오후 {}:{}'.format(current_time.strftime("%I"), current_time.strftime("%M"))

        return render(request, self.template_name, {'nowtime':nowtime})


def test(request):
    stations = Station.objects.all()
    tourspots = Tourspot.objects.all()
    congestions = Congestion.objects.all()
    return render(request, 'subway/test.html', {'stations': stations, 'tourspots': tourspots,'congestions': congestions})