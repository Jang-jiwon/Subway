import requests

# getLocationInfo 결과 sample
API_KEY = 'ddD0JPaBMHkAte/oudaImNRJlg9h9uvLoKMIOtZPLqjO3AtVkQW2m2r1La8fv7xFrm9MqauC1PpS6vnuiHj13w=='

url = 'http://ws.bus.go.kr/api/rest/pathinfo/getLocationInfo'
params ={'serviceKey' : API_KEY,
         'stSrch' : '왕십리역', 'resultType' : 'json'}

response = requests.get(url, params=params)
result = response.json()['msgBody']['itemList']

for i in result :
    print('--------------------------------------------')
    print('[1] POI ID : ' + i['poiId'])
    print('[2] POI 이름 : ' + i['poiNm'])
    print('[3] X좌표 : ' + i['gpsX'])
    print('[4] Y좌표 : ' + i['gpsY'])
    print('[5] X좌표 : ' + i['posX'])
    print('[6] Y좌표 : ' + i['posY'])

