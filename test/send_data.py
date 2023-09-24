import requests

<<<<<<< Updated upstream
#url = "http://13.125.205.99/register" #서버 테스트
url = "http://127.0.0.1:7777/get_string" #로컬 테스트
#data = {"x": 35.834344,"y": 128.755423} #gps 테스트 좌표 (대학교)
#data = {"x": 35.832704,"y": 128.735329} #gps 테스트 좌표 (마트)
data = {"key" : "현금 영수증 필요하세요?."} #AI 음성인식 테스트 텍스트
#data = {"name" : "AWSTest", 'phone': '01040046666', 'password' : 'test1234'}  #회원가입 테스트
#data = { 'phone': '01020023003', 'password' : 'test1234'}  #로그인 테스트
#data = { 'phone': '01088889999', 'fav' : ['네 맞워요', '아닌데요', '몰?루']}  #즐겨찾기 정보 저장 테스트
#data = { 'phone': '01088889999'}  #즐겨찾기 정보 불러오기 테스트
=======
url = "http://13.125.205.99/get_gps" #서버 테스트
#url = "http://127.0.0.1:7777/get_gps" #로컬 테스트
#data = {"x": 35.834344,"y": 128.755423} #gps 테스트 좌표 (대학교)
#data = {"x": 35.834822,"y": 128.732897} #gps 테스트 좌표 (대학교)
data = {"x": 35.832704,"y": 128.735329} #gps 테스트 좌표 (마트)
#data = {"key" : "카드 결제로 하고 싶어요."} #AI 음성인식 테스트 텍스트
#data = {"name" : "AWSTestAccV2", 'phone': '01099998888', 'password' : 'test1234'}  #회원가입 테스트
#data = { 'phone': '01020023003', 'password' : 'test1234'}  #로그인 테스트
#data = { 'phone': '01099998888', 'fav' : ['네 맞워요', '아닌데요', '몰?루','AWS 추가 테스트 test2']}  #즐겨찾기 정보 저장 테스트
#data = { 'phone': '01099998888'}  #즐겨찾기 정보 불러오기 테스트
>>>>>>> Stashed changes
response = requests.post(url, json=data)
print(response)

print(response.json())
