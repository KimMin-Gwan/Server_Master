import requests

#url = "http://13.125.205.99/get_string" #서버 테스트
url = "http://127.0.0.1:7777/login" #로컬 테스트
#data = {"x": 35.834344,"y": 128.755423} #gps 테스트 좌표 (대학교)
#data = {"x": 35.832704,"y": 128.735329} #gps 테스트 좌표 (마트)
#data = {"key" : "카드 결제로 하고 싶어요."} #AI 음성인식 테스트 텍스트
#data = {"name" : "test", 'phone': '01000000000', 'password' : 'test1234'} 
data = { 'phone': '01000000000', 'password' : 'test1234'} 
response = requests.post(url, json=data)
print(response)

print(response.json())
