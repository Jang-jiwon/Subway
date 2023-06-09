import pandas as pd
# csv파일에서 역명으로 역코드 검색

# 전철역 코드 csv 읽음
pd.set_option('display.max_columns', None)
subwaycode = pd.read_csv('subwaycode.csv', names=["호선","상/하행선","요일","전철역코드","외부코드","전철역명","첫차시간","첫차출발역코드","첫차도착역코드","첫차출발역명","첫차도착역명","막차시간","막차출발역코드","막차도착역코드","막차출발역명","막차도착역명"], encoding='CP949')

# 역이름으로 변수 받기
stationNM = input('코드를 찾을 역 이름 입력')

# 전철역명과 받은 변수가 같은 dataFrame
stationDT = subwaycode.loc[(subwaycode['전철역명'] == stationNM)]

# 첫번째 행에서 출력
print('전철역코드 : {} | 외부코드 : {}'.format(stationDT.iloc[0]["전철역코드"],stationDT.iloc[0]["외부코드"]))