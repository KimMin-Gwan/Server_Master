import requests
from urllib.parse import urlparse
import json

headers = {'application/json'}


areaLLCode = '11'   #String 선택 지역 대분류 코드입니다.    searchType=name로 하여 검색 할 경우에는 필수로 입력해야 합니다.
areaLMCode = '440'  #String 선택 지역 중분류 코드입니다. searchType=name로 하여 검색 할 경우에는 필수로 입력해야 합니다.
resCoordType ='WGS84GEO'    #String 선택 좌표계 유형을 지정 WGS84GEO경위도
searchType = 'all'   #String	선택
searchtypCd = 'A'    #거리순, 정확도순 검색 A: 정확도순  R : 거리순 'R' 거리순을 선택할 경우 radius(검색반경) 필수
radius = '0'     #검색반경(1~33) 단위 “1” = 1km 전국 반경으로 검색 시 단위 “0” 입력
reqCoordType = 'WGS84GEO'   #입력 하는 좌표계 유형을 지정
centerLon ='128.755423'  #반경 검색에서 사용하는 중심 좌표의 경도 좌표입니다. * 검색종류 '거리순' 일경우 필수
centerLat ='35.834344'  #반경 검색에서 사용하는 중심 좌표의 위도 좌표입니다. * 검색종류 '거리순' 일경우 필수
lat = '35.825852'
lon = '128.736590'
multiPoint = 'N'     #String 멀티입구점 미지원 여부.
callback  =''  #jsonp 포맷에서 사용하는 callback 함수명 정보입니다. application/javascript 일 때 필수로 입력해야 합니다.
fullAddr = '경상북도 경산시 경안로67길 14'
addressFlag = 'F02'


#
#주소로 검색
#url = f'https://apis.openapi.sk.com/tmap/geo/fullAddrGeo?addressFlag={addressFlag}&version={version}&fullAddr={fullAddr}&appKey={appKey}'
#좌표검색? X
#url = f'https://apis.openapi.sk.com/tmap/geo/reversegeocoding?version={version}&lat={lat}&lon={lon}&appKey={appKey}'

#  "searchKeyword" : "주유소", #searchType 이 keyword 인 경우 필수, 경로 반경 내 특정 키워드를 검색할 경우.
#  #경로 궤적 정보.X 좌표, Y 좌표를 콤마(,)와 밑줄(_)로 구분하여 순서대로 나열합니다.
#result = requests.get(url,headers = headers).json()
#r



def get_biz_name():
  #장소 정보
  
  version = 1
  page = 1   #Number	선택	조회할 목록의 페이지를 지정합니다.
  count = 3	    #Number	선택	페이지당 출력되는 개수를 지정합니다.
  searchKeyword ="영남대학교 이희건기념관"	    #String 필수	 전화번호 검색(searchType=telno) 명칭 검색(searchType=name)
  appKey = '___________'

  url = f'https://apis.openapi.sk.com/tmap/pois?version={version}&page={page}&count={count}&searchKeyword={searchKeyword}&appKey={appKey}'

  result = requests.get(url).json()
  print(json.dumps(result["searchPoiInfo"]['pois']['poi'][0]['lowerBizName'],indent=4,ensure_ascii=False))

def get_name():
  version = 1
  y = '35.832704'
  x = '128.735329'
  appKey = '________'
  lineString = x +',' + y  +'_' + x + ',' + y
  payload = {
    "startX" : x, #출발지 X좌표입니다.
    "startY" : y, #출발지 Y좌표입니다.
    "endX" : x, #목적지 X좌표입니다.
    "endY" : y, #목적지 Y좌표입니다.
    "userX" : x, #사용자의 현재 X좌표입니다.
    "userY" : y, #사용자의 현재 Y좌표입니다.
    "sort"  : "distance", #검색 결과 정렬. • score : 랭킹 점수 높은순 (default) • distance : 가까운 거리순 • evcharger : 가까운 거리 내 사용 가능한 EV 충전기 많은순
    "page" : "1", #조회할 목록의 페이지를 지정합니다.
    "count" : "10", #페이지당 출력되는 개수를 지정합니다.
    "radius" : "0.1", #km 단위 검색 반경.
    "searchType" : "nearby", # keyword - 일반 키워드 검색 / category - 카테고리검색 (키워드 없음) / nearby - 근처검색( 키워드 없음)
    "lineString" : lineString
  }

  #payload
  url = f'https://apis.openapi.sk.com/tmap/poi/findPoiRoute?version={version}&appKey={appKey}'

  result = requests.post(url, json = payload).json()
  for i in result["searchPoiInfo"]['pois']['poi']:
    print(json.dumps(i['name'],indent=4,ensure_ascii=False))
  

get_biz_name()