import requests
from urllib.parse import urlparse
import json
import back_end

class GPS():   
    def __init__(self, x, y):
        self.x = y
        self.y = x


    def __get_location_name(self): #이건됨
        #gps 경도 위도로 현재 위치의 정보 받기
        name_list = []
        payload = {
            "startX" : self.x, #출발지 X좌표입니다.
            "startY" : self.y, #출발지 Y좌표입니다.
            "endX" : self.x, #목적지 X좌표입니다.
            "endY" : self.y, #목적지 Y좌표입니다.
            "userX" : self.x, #사용자의 현재 X좌표입니다.
            "userY" : self.y, #사용자의 현재 Y좌표입니다.
            "sort"  : "distance", #검색 결과 정렬. • score : 랭킹 점수 높은순 (default) • distance : 가까운 거리순 • evcharger : 가까운 거리 내 사용 가능한 EV 충전기 많은순
            "page" : "1", #조회할 목록의 페이지를 지정합니다.
            "count" : "1", #페이지당 출력되는 개수를 지정합니다.
            "radius" : "0.1", #km 단위 검색 반경.
            "searchType" : "nearby", # keyword - 일반 키워드 검색 / category - 카테고리검색 (키워드 없음) / nearby - 근처검색( 키워드 없음)
            "lineString" : f'{self.x},{self.y}_{self.x},{self.y}'
        }

        try:
            url = f'https://apis.openapi.sk.com/tmap/poi/findPoiRoute?version={back_end.constant.tmap_version}&appKey={back_end.constant.tmap_key}'

            result = requests.post(url, json = payload).json()
            # for i in result["searchPoiInfo"]['pois']['poi']:
            #     name_list.append(json.dumps(i['name'],ensure_ascii=False))
            # return name_list
            return result["searchPoiInfo"]['pois']['poi'][0]['name']
        except:
            return "error not found"

    def __get_location_biz_name(self): #이게안됨 여러개 말고 단일로 하나만 보내봐야 할듯
        #건물 이름으로 얻은 데이터 분석해서 장소 보내주기 
        biz_name_list = []      
        page = 1   #Number	선택	조회할 목록의 페이지를 지정합니다.
        count = 1	    #Number	선택	페이지당 출력되는 개수를 지정합니다.
        try:
            biz_name_list = self.__get_location_name()
            for i in biz_name_list:
                url = f'https://apis.openapi.sk.com/tmap/pois?version={back_end.constant.tmap_version}&page={page}&count={count}&searchKeyword={i}&appKey={back_end.constant.tmap_key}'
                result = requests.get(url).json()
                biz_name_list.append(json.dumps(result["searchPoiInfo"]['pois']['poi'][0]['lowerBizName'],ensure_ascii=False))
            return biz_name_list
        except:
            return "default"



    def gps_analyzer(self):
        #건물 이름으로 얻은 데이터 분석해서 장소 라벨 보내주기 ex)식당, 병원, 약국, 학교
        headers = back_end.constant.naver_headers
        #headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}
        url_base="https://openapi.naver.com/v1/search/local.json?query="
        keyword = self.__get_location_name()
        url_middle="$&start="
        number='1'

        url = url_base + keyword + url_middle + number
        if(keyword == "error not found"):
            result_json = {'category': 'default'}
            return result_json

        with open (back_end.constant.AAC_FILE, "r", encoding='cp949') as f:
                saved_data = json.load(f)



        result = requests.get(url,headers = back_end.constant.naver_headers).json()
        try:
            #BdUse = json.dumps(result['items'][0]["category"],indent=4,ensure_ascii=False)
            BdUse = result['items'][0].pop('category', None)
            # data_temp = BdUse.split('>')
            # data= data_temp.split(',')
            data = BdUse.split('>')
            data = data[0].split(',')
            data = data[0]
            # for i in saved_data["AAC"]:
            #     if(i["name"]==data[-1]):
            #         result_json = {'category': data[-1]}
            #         break;
            #     else:
            #         result_json = {'category': 'default'}
            result_json = {'category': data}
            return result_json
        except:
            result_json = {'category': 'default'}
            return result_json
        
