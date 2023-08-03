import requests

url = "http://13.125.205.99/get_gps" #서버 테스트
#url = "http://127.0.0.1:7777/get_gps" #로컬 테스트
data = {"x": 35.834344,"y": 128.755423} #gps 테스트 좌표 (대학교)
#data = {"x": 35.832704,"y": 128.735329} #gps 테스트 좌표 (마트)
#data = {"key" : "카드 결제로 하고 싶어요."} #AI 음성인식 테스트 텍스트
response = requests.post(url, json=data)
print(response)

print(response.json())
