import requests
import pandas as pd

# 지하철역 코드 csv 읽음
stations = pd.read_csv('stationcode.csv', names=["SUBWAY_ID", "STATN_ID", "STATN_NM", "호선이름"], encoding='utf-8')
# print(stations)

# 요청 url - http://swopenAPI.seoul.go.kr/api/subway/ 요청 키 / json 형식 / n번째 row부터 / n번째 row까지 / 역 이름으로 검색
url = 'http://swopenAPI.seoul.go.kr/api/subway/5878626661646d7337395068797661/json/realtimeStationArrival/0/100/서울'

# json 형식 데이터 획득 
response = requests.get(url)
data = response.json()
list = data['realtimeArrivalList']

# 호선코드, 도착코드 딕셔너리
subwayId = {'1001':'1호선', '1002':'2호선', '1003':'3호선', '1004':'4호선', '1005':'5호선',
            '1006':'6호선', '1007':'7호선', '1008':'8호선', '1009':'9호선', '1061':'중앙선',
            '1063':'경의중앙선', '1065':'공항철도', '1067':'경춘선', '1075':'수의분당선', '1077':'신분당선', '1092':'우이신설선'}
arvlCd = {'0':'진입', '1':'도착', '2':'출발', '3':'전역출발', '4':'전역진입', '5':'전역도착', '99':'운행중'}

# 응답 전체 출력 
for i in list:
    
    print('--------'+str(i['rowNum'])+'--------')
    print('[1] 지하철 호선 id : ' + i['subwayId'] + '-' + subwayId[i['subwayId']])
    print('[2] 상행/하행 : ' + i['updnLine'])
    print('[3] 도착지 방면 : ' + i['trainLineNm'])
    # [4]열 부재 
    
    print('[5] 이전 지하철역 id : ' + i['statnFid'])
    print(stations.loc[(stations['STATN_ID'] == i['statnFid'])])
    print('[6] 다음 지하철역 id : ' + i['statnTid'])
    print(stations.loc[(stations['STATN_ID'] == i['statnTid'])])
    print('[7] 지하철역 id : ' + i['statnId'])
    print(stations.loc[(stations['STATN_ID'] == i['statnId'])])
    
    # 공통 row --------------------------------------------------------
    print('[8] 지하철역명 : ' + i['statnNm'])
    print('[9] 환승 노선 수 : ' + i['trnsitCo'])
    # ----------------------------------------------------------------
    
    # (상하행코드(1자리), 순번(첫번째, 두번째 열차 , 1자리), 첫번째 도착예정 정류장 - 현재 정류장(3자리), 목적지 정류장, 급행여부(1자리))
    print('[10] 도착예정열차순번 : ' + i['ordkey'])
    
    # 공통 row --------------------------------------------------------
    print('[11] 연계호선 id : ' + i['subwayList'])
    print('[12] 연계지하철역 id : ' + i['statnList'])
    # ----------------------------------------------------------------
    
    print('[13] 열차 종류 : ' + i['btrainSttus'])
    sc = int(i['barvlDt'])
    print('[14] 도착 예정 시간 : ' + str(int(sc/60)) + '분 ' + str(sc%60) + '초')
    print('[15] 열차 번호 : ' + i['btrainNo'])
    print('[16] 종착지하철역 id : ' + i['bstatnId'])
    print('[17] 종착지하철역명 : ' + i['bstatnNm'])
    
    print('[18] 도착정보 생성시각 : ' + i['recptnDt'])
    print('[19] 도착메시지 1 : ' + i['arvlMsg2'])
    print('[20] 도착메시지 2 : ' + i['arvlMsg3'])
    print('[21] 도착 코드 : ' + i['arvlCd'] + '-' + arvlCd[i['arvlCd']])


