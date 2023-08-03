import requests

url = "http://13.125.205.99/get_gps"
data = {"x": 35.834344,"y": 128.755423} #gps 테스트 좌표 (영남대)
#data = {"key" : "카드 결제로 하고 싶어요."} #AI 음성인식 테스트 텍스트
response = requests.post(url, json=data)
print(response)

print(response.json())
