from datetime import datetime
from operator import itemgetter

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

        timeurl = 'http://openapi.seoul.go.kr:8088/736f67684a646d733339556f7a726d/json/SearchSTNTimeTableByIDService/1/250/'
        arrivalurl = 'http://swopenAPI.seoul.go.kr/api/subway/5878626661646d7337395068797661/json/realtimeStationArrival/0/100/'

        if self.kwargs.get('code') :
            station = Station.objects.get(station_code=self.kwargs['code'])
            context['station'] = station
            timeurl += '%04d'%(station.station_code)+'/'
            arrivalurl += station.station_name.rstrip('역')

            linecode = '100' + str(station.line.serial_number)
        else :
            context['station'] = stations[0]
            timeurl += '%04d' % (stations[0].station_code) + '/'
            arrivalurl += stations[0].station_name.rstrip('역')
            linecode = '100' + str(stations[0].line.serial_number)

        timetable = dict()

        days = {'1': '평일', '2': '토요일', '3': '휴일/일요일'}
        inouts = {'1': '상행', '2': '하행'}

        for day in days:
            sub_table = dict()
            for inout in inouts:
                response = requests.get('{}{}/{}/'.format(timeurl, day, inout))
                data = response.json()
                list = data['SearchSTNTimeTableByIDService']['row']

                sub_table[inout] = list

            timetable[day] = sub_table

        context['timetable'] = timetable

        response = requests.get(arrivalurl)
        data = response.json()
        list = data['realtimeArrivalList']

        arrival = dict()
        uplist = []
        dnlist = []
        arvlCd = {'0': '진입', '1': '도착', '2': '출발', '3': '전역출발', '4': '전역진입', '5': '전역도착', '99': '운행중'}

        for row in list :
            row['order'] = str(row['ordkey'][2:5])
            row['toStation'] = row['trainLineNm'].split('-')[0].lstrip()
            if row['arvlCd'] == '0':
                row['message'] = '진입중'
            elif row['arvlCd'] == '1':
                row['message'] = '현재 역 도착'
            elif row['arvlCd'] == '2':
                row['message'] = '현재 역 출발'
            elif row['arvlCd'] == '3':
                row['message'] = '전역 출발'
            elif row['arvlCd'] == '4':
                row['message'] = '전역 진입'
            elif row['arvlCd'] == '5':
                row['message'] = '전역 도착'
            elif row['arvlCd'] == '99':
                if row['barvlDt'] != '0':
                    row['message'] = str(int(row['barvlDt']) % 60) + '분 후 도착'
                else :
                    row['message'] = str(row['ordkey'][2:5]).lstrip('0') + '개 전 역 도착'

        for row in list :
            if row['subwayId'] == linecode :
                if row['updnLine'] == '상행' :
                    uplist.append(row)
                elif row['updnLine'] == '하행' :
                    dnlist.append(row)

        arrival['up'] = sorted(uplist, key=itemgetter('order'))
        arrival['dn'] = sorted(dnlist, key=itemgetter('order'))

        # print(arrival)
        context['arrival'] = arrival

        return context

def test(request):
    stations = Station.objects.all()
    tourspots = Tourspot.objects.all()
    congestions = Congestion.objects.all()
    url = 'http://swopenAPI.seoul.go.kr/api/subway/5878626661646d7337395068797661/json/realtimeStationArrival/0/100/삼각지'
    response = requests.get(url)
    data = response.json()
    list = data['realtimeArrivalList']

    return render(request, 'subway/test.html', {'stations': stations, 'tourspots': tourspots,'congestions': congestions,
                                                'list':list} )

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