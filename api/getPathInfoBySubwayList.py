import requests
import pandas as pd

# getPathInfoBySubway로 경로 구하기
# 역사좌표 코드 csv 읽음
pd.set_option('display.max_columns', None)
subwayXY = pd.read_csv('subwayXY.csv', names=['연번','호선','고유역번호(외부역코드)','역명','위도','경도','작성일자'], encoding='CP949')

API_KEY = 'ddD0JPaBMHkAte/oudaImNRJlg9h9uvLoKMIOtZPLqjO3AtVkQW2m2r1La8fv7xFrm9MqauC1PpS6vnuiHj13w=='

# 시작점 받기
startPOI = input('시작점을 입력하세요').strip()
startST = subwayXY.loc[(subwayXY['역명'] == startPOI)]
startX = startST.iloc[0]['경도']
startY = startST.iloc[0]['위도']
print(startX, startY)

# 도착점 받기
endPOI = input('도착점을 입력하세요').strip()
endST = subwayXY.loc[(subwayXY['역명'] == endPOI)]
endX = endST.iloc[0]['경도']
endY = endST.iloc[0]['위도']
print(endX, endY)

url = 'http://ws.bus.go.kr/api/rest/pathinfo/getPathInfoBySubway'
params ={'serviceKey' : API_KEY, 'startX' : startX , 'startY' : startY,
    'endX': endX , 'endY': endY, 'resultType' : 'json'}
response = requests.get(url, params=params)
result = response.json()['msgBody']['itemList']
index = 0
for i in result :
    index += 1
    print('-------- ' + str(index) + '번 경로 --------')
    print('[1] 소요 시간 : ' + i['time'] + '분')
    print('[2] 거리 : ' + i['distance'])
    print('[3] 환승 횟수 : ' + str(len(i['pathList'])-1))
    r_index = 0
    for l in i['pathList'] :
        r_index += 1
        print('({}) {} {} 탑승 - {} 하차, {}개 역 이동'.format(r_index,l['routeNm'],l['fname'],l['tname'],len(l['railLinkList'])))