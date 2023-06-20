from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.views.generic import View, DetailView, ListView

from .models import Station, Congestion, Tourspot


def index(request):
    # return render(request, 'subway/test.html')
    return redirect('/map/')
    # return redirect('subway:map')


def map(request):
    return render(request, 'subway/map.html')

# def detail(request):
#     return render(request, 'subway/stationdetail.html')

class detail(ListView) :
    template_name = 'subway/stationdetail.html'
    model = Station
    def get_context_data(self, **kwargs):

        ids = self.kwargs['id'].split('x')
        stations = []
        for id in ids :
            stations.append(Station.objects.get(station_code=id))

        current_time = datetime.now()
        nowtime = ''
        if current_time.strftime("%p") == 'AM':
            nowtime = '오전 {}:{}'.format(current_time.strftime("%I"), current_time.strftime("%M"))
        elif current_time.strftime("%p") == 'PM':
            nowtime = '오후 {}:{}'.format(current_time.strftime("%I"), current_time.strftime("%M"))

        context = super(detail, self).get_context_data()
        context['nowtime'] = nowtime
        context['ids'] = ids
        context['stations'] = stations

        if self.kwargs.get('code') :
            context['station'] = Station.objects.get(station_code=self.kwargs['code'])
        else :
            context['station'] = stations[0]

        return context
    # def get(self, request):
    #
    #     current_time = datetime.now()
    #     nowtime = ''
    #     if current_time.strftime("%p") == 'AM':
    #         nowtime = '오전 {}:{}'.format(current_time.strftime("%I"), current_time.strftime("%M"))
    #     elif current_time.strftime("%p") == 'PM':
    #         nowtime = '오후 {}:{}'.format(current_time.strftime("%I"), current_time.strftime("%M"))
    #
    #     ids = request.GET.get('id').split('x')
    #
    #     return render(request, self.template_name, {'nowtime': nowtime, 'ids': ids})


def test(request):
    stations = Station.objects.all()
    tourspots = Tourspot.objects.all()
    congestions = Congestion.objects.all()
    return render(request, 'subway/test.html', {'stations': stations, 'tourspots': tourspots,'congestions': congestions})