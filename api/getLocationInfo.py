import requests
from urllib.parse import urlencode, quote_plus

API_KEY = 'ddD0JPaBMHkAte%2FoudaImNRJlg9h9uvLoKMIOtZPLqjO3AtVkQW2m2r1La8fv7xFrm9MqauC1PpS6vnuiHj13w%3D%3D'
print(API_KEY)

url = 'http://ws.bus.go.kr/api/rest/pathinfo/getLocationInfo'
params ={'serviceKey' : API_KEY,
         'stSrch' : '광화문', 'resultType' : 'json'}

response = requests.get(url, params=params)
print(response.content)