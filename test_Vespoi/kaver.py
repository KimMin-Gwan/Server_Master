import requests
from urllib.parse import urlparse
import json

client_id = '_________________' 
client_secret = '_______________'
naver_headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}
kakao_headers={"Authorization": "KakaoAK _________________"} 

test_lat = 128.693185
test_lon = 35.868442

def getBuildName(lat, lon):
    url = f"https://dapi.kakao.com/v2/local/geo/coord2address.json?x={lat}&y={lon}"

   
    try :
        result = requests.get(urlparse(url).geturl(),
        headers=kakao_headers).json()
        #BD_name = json.dumps(result,indent=4,ensure_ascii=False)
        BD_name = json.dumps(result['documents'][0]["road_address"]["building_name"],indent=4,ensure_ascii=False)

        return BD_name

    except:
        err = "error not found"
        return err
   

def getBuildUse(name):
    headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}

    url_base="https://openapi.naver.com/v1/search/local.json?query="
    keyword = name
    url_middle="$&start="
    number='1'

    if(name == "error not found"):
        err = "failled to find bd use"
        return err

    url = url_base + keyword + url_middle + number
    result = requests.get(url,headers = naver_headers).json()
    #BdUse = json.dumps(result['items'][0]["category"],indent=4,ensure_ascii=False)
    BdUse = result['items'][0].pop('category', None)
    data = BdUse.split('>')
    result_json = {'category': data[1]}

    return result_json

    



test_name = getBuildName(test_lat,test_lon)
print(test_name)
print(getBuildUse(test_name))