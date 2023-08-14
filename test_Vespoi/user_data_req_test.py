#저장하는게 있으면 불러오는거도 있어야지
#그냥 DB에서 폰 번호 찾아서 거기에 붙어있는 즐겨찾기 데이터 가져오면 됨
import requests
from urllib.parse import urlparse
import json
from pymongo import MongoClient
import certifi

mongo_connect = "mongodb+srv://admin:r3tgCfkESORu8iO4@cluster0.pmbm4ny.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_connect, tlsCAFile=certifi.where())
db = client.temp

phone = '01088889999'
try:
    db_data = list(db.user_data.find({'phone':{'$regex': phone}}))
    user_data = dict(db_data[0])
    fav_data = user_data['fav']

    response = {"message":fav_data} 
    print (response)

except:
    response = {"message":"unknown error"}
    print( response )