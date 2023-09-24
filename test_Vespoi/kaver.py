import requests
from urllib.parse import urlparse
import json

client_id = 'U_JVe8czFTPTdfOU_7Fs' 
client_secret = 'ZBiUd0rclE'
naver_headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}
kakao_headers={"Authorization": "KakaoAK 468b7fd043830d2a5ddb6fff0a000b5b"} 

test_lat = 128.735329
test_lon = 35.832704

def getBuildName(lat, lon):
    url = f"https://dapi.kakao.com/v2/local/geo/coord2address.json?x={lat}&y={lon}"

   
    try :
        result = requests.get(urlparse(url).geturl(),
        headers=kakao_headers).json()
        #BD_name = json.dumps(result,indent=4,ensure_ascii=False)
        BD_name = json.dumps(result['documents'][0]["road_address"]["building_name"],indent=4,ensure_ascii=False)

        return BD_name

    except:
        return json.dumps(result,indent=4,ensure_ascii=False)
   

def getBuildUse(name):
    headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}

    url_base="https://openapi.naver.com/v1/search/local.json?query="
    keyword = name
    url_middle="$&start="
    number='1'

    with open ("C:/Users/for/Study/ComPass/Back_Test/Server_Master/python/json_data_test.json", "r") as f:
            saved_data = json.load(f)

    url = url_base + keyword + url_middle + number
    result = requests.get(url,headers = naver_headers).json()
    try:
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
                        print(data_second[1])
                        result_json = {'category': data_second[1]}
            except:
                result_json = {'category': 'default'}

        return result_json
    except:
            result_json = {'category': 'default'}
            return result_json


test_name = getBuildName(test_lat,test_lon)
print(test_name)
print(getBuildUse(test_name))