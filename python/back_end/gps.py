import requests
from urllib.parse import urlparse
import json
import back_end

class GPS():   
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __get_location(self):
        #gps 경도 위도로 현재 위치의 정보 받기
        url = f"https://dapi.kakao.com/v2/local/geo/coord2address.json?x={self.y}&y={self.x}"
        result = requests.get(urlparse(url).geturl(), headers=back_end.constant.kakao_headers).json()        
        return result

    def __location_name(self): #받아온 json 데이터에서 건물 이름을 뽑아냄
        try:
            data = json.dumps(self.__get_location()['documents'][0]["road_address"]["building_name"],
                              indent=4,ensure_ascii=False)
            return data
        
        except:
            err = "error not found"
            return err #나중에 수정 해야됨  ex) 건물 이름 정보를 찾을 수 없습니다.


    def gps_analyzer(self):
        #건물 이름으로 얻은 데이터 분석해서 장소 라벨 보내주기 ex)식당, 병원, 약국, 학교
        headers = back_end.constant.naver_headers
        #headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}

        url_base="https://openapi.naver.com/v1/search/local.json?query="
        keyword = self.__location_name()
        url_middle="$&start="
        number='1'

        url = url_base + keyword + url_middle + number
        if(keyword == "error not found"):
            result_json = {'category': 'default'}
            return result_json

        with open ("json_data_test.json", "r", encoding='cp949') as f:
                saved_data = json.load(f)
        
        result = requests.get(url,headers = back_end.constant.naver_headers).json()
        try:
            #BdUse = json.dumps(result['items'][0]["category"],indent=4,ensure_ascii=False)
            BdUse = result['items'][0].pop('category', None)
            data_first = BdUse.split('>')
            data_second = data_first[1].split(',')

            for i in saved_data["AAC"]:
                if(i["name"]==data_second):
                    data = data_second



            if(len(data_second)== 1):
                try:
                    for i in saved_data["AAC"]:
                        if(i["name"]==data_second[0]):
                            result_json = {'category': data_second[0]}
                except:
                    result_json = {'category': 'default'}
            elif(len(data_second)== 2):
                try:
                    for i in saved_data["AAC"]:
                        if(i["name"]==data_second[1]):
                            result_json = {'category': data_second[1]}
                except:
                    result_json = {'category': 'default'}

            return result_json
        except:
            result_json = {'category': 'default'}
            return result_json
        
