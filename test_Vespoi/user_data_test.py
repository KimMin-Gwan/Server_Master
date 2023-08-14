#여기에 만들거는 음.. 즐겨찾기 정보 저장하기?
#받는건 유저 폰 번호랑 저장 할 거
#폰 번호는 그냥 int든 string이든 받고 즐겨찾기는 list 딕셔너리로 fav: ['ㅇㅇ', 'ㄴㄴ', '몰루']
#정보 확인은 어차피 로그인 할 떄 하니까 그냥 저장하면 될듯 대신 추가가 아닌 update를 해야댐
import requests
from urllib.parse import urlparse
import json
from pymongo import MongoClient
import certifi

mongo_connect = "mongodb+srv://admin:r3tgCfkESORu8iO4@cluster0.pmbm4ny.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_connect, tlsCAFile=certifi.where())
db = client.temp

phone = '01088889999'
fav_data = ['네 맞워요', '아닌데요', '몰?루']
try:
    db.user_data.update_one({"phone" :phone},{'$set' : {"fav":fav_data}})

    response = {"message":"saved"} 
    print (response)

except:
    response = {"message":"unknown error"}
    print( response )
    