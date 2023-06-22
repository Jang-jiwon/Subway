from datetime import datetime

from django.db.models import Q
import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.views.generic import View, DetailView, ListView

from .models import Line, Station, Congestion, Tourspot


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

        url = 'http://openapi.seoul.go.kr:8088/736f67684a646d733339556f7a726d/json/SearchSTNTimeTableByIDService/1/250/'

        if self.kwargs.get('code') :
            station = Station.objects.get(station_code=self.kwargs['code'])
            context['station'] = station
            url += '%04d'%(station.station_code)+'/'

        else :
            context['station'] = stations[0]
            url += '%04d' % (stations[0].station_code) + '/'

        timetable = dict()

        days = {'1': '평일', '2': '토요일', '3': '휴일/일요일'}
        inouts = {'1': '상행', '2': '하행'}

        for day in days:
            sub_table = dict()
            for inout in inouts:
                response = requests.get('{}{}/{}/'.format(url, day, inout))
                data = response.json()
                list = data['SearchSTNTimeTableByIDService']['row']

                sub_table[inout] = list

            timetable[day] = sub_table

        context['timetable'] = timetable

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

    url = 'http://openapi.seoul.go.kr:8088/736f67684a646d733339556f7a726d/json/SearchSTNTimeTableByIDService/1/250/0428/'

    # 외부역코드 검색시 url - 서비스명, 코드 부분만 다름
    # http://openAPI.seoul.go.kr:8088/(인증키)/json/SearchSTNTimeTableByFRCodeService/1/5/132/1/1/

    timetable = dict()
    # 요일, 상/하행, 급행 딕셔너리
    days = {'1': '평일', '2': '토요일', '3': '휴일/일요일'}
    inouts = {'1': '상행', '2': '하행'}
    directYN = {'G': '일반(general)', 'D': '급행(direct)'}

    for day in days:
        print(day)
        sub_table = dict()
        for inout in inouts:
            print(inout)
            response = requests.get('{}{}/{}/'.format(url, day, inout))
            print('{}{}/{}/'.format(url, day, inout))
            data = response.json()
            list = data['SearchSTNTimeTableByIDService']['row']

            sub_table[inout] = list

        timetable[day] = sub_table

    # print(timetable)
    return render(request, 'subway/test.html', {'stations': stations, 'tourspots': tourspots,'congestions': congestions,
                                                'timetable': timetable})
def SearchId(request, q):
    try:
        stations = Station.objects.filter(station_name=q)
        if stations.exists():
            stationIds = [station.station_code for station in stations]
            return JsonResponse({'stationIds': stationIds})
        else:
            return JsonResponse({'stationIds': []})
    except Station.DoesNotExist:
        return JsonResponse({'stationIds': []})


def SearchStation(request, id):
    ids = id.split('x')
    stations = []
    for id in ids:
        stations.append(Station.objects.get(station_code=id))

    stationjson = {}
    for station in stations :
        sub_station = {}
        sub_station['line'] = station.line.serial_number
        sub_station['name'] = station.station_name
        stationjson[station.station_code] = sub_station

    return JsonResponse(stationjson)