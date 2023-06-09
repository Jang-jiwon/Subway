import requests

# 요청 url - http://sopenapi.seoul.go.kr:8088/ 요청 키 / json 형식 / SearchSTNTimeTableByIDService / n번째 row부터 / n번째 row까지
# / 역 코드 / 요일(1-평일 , 2-토요일, 3-휴일/일요일) / 상행,하행(1-상행, 2-하행)
# 예시 - 삼각지 평일 상행 시간표
url = 'http://openapi.seoul.go.kr:8088/736f67684a646d733339556f7a726d/json/SearchSTNTimeTableByIDService/1/250/0428/1/1/'

# 외부역코드 검색시 url - 서비스명, 코드 부분만 다름
# http://openAPI.seoul.go.kr:8088/(인증키)/json/SearchSTNTimeTableByFRCodeService/1/5/132/1/1/

# json 형식 데이터 획득 
response = requests.get(url)
data = response.json()
list = data['SearchSTNTimeTableByIDService']['row']
# print(list)
idx = 0;

# 요일, 상/하행, 급행 딕셔너리
day = {'1':'평일', '2':'토요일', '3':'휴일/일요일'}
inout = {'1':'상행', '2':'하행'}
directYN = {'G':'일반(general)', 'D':'급행(direct)'}

# 응답 전체 출력
# for i in list:
#     idx += 1
#     print('----------------'+str(idx)+'----------------')
#     print('[1] 호선 : ' + i['LINE_NUM'])
#     # 외부코드 : 역 이름과 함께 적혀있는 역번호
#     print('[2] 외부코드 : ' + i['FR_CODE'])
#     print('[3] 전철역코드 : ' + i['STATION_CD'])
#     print('[4] 전철역명 : ' + i['STATION_NM'])
#     print('[5] 열차번호 : ' + i['TRAIN_NO'])
#     print('[6] 도착시간 : ' + i['ARRIVETIME'])
#     print('[7] 출발시간 : ' + i['LEFTTIME'])
#     print('[8] 출발지하철역코드 : ' + i['ORIGINSTATION'])
#     print('[9] 도착지하철역코드 : ' + i['DESTSTATION'])
#     print('[10] 출발지하철역명 : ' + i['SUBWAYSNAME'])
#     print('[11] 도착지하철역명 : ' + i['SUBWAYENAME'])
#     print('[12] 요일 : ' + i['WEEK_TAG'] + '-' + day[i['WEEK_TAG']])
#     print('[13] 상/하행 : ' + i['INOUT_TAG'] + '-' + inout[i['INOUT_TAG']])
#     print('[14] 플러그 : ' + i['FL_FLAG'])
#     print('[15] 도착역 코드 2 : ' + i['DESTSTATION2'])
#     print('[16] 급행 여부 : ' + i['EXPRESS_YN'] + '-' + directYN[i['EXPRESS_YN']])
#     print('[17] 지선 : ' + i['BRANCH_LINE'])

# 호선 / 역명 / 요일 / 상하행
print(list[0]['LINE_NUM'], list[0]['STATION_NM'], day[list[0]['WEEK_TAG']], inout[list[0]['INOUT_TAG']] )
for i in list:
    idx += 1
    print('[{}] 열차번호 : {} | 도착시간 : {} | 출발시간 : {} | {}행 | {}'
          .format(idx, i['TRAIN_NO'],i['ARRIVETIME'],i['LEFTTIME'],i['SUBWAYENAME'],directYN[i['EXPRESS_YN']]))

