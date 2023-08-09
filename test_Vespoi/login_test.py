import requests
from urllib.parse import urlparse
import json
from pymongo import MongoClient
import certifi

mongo_connect = "mongodb+srv://admin:r3tgCfkESORu8iO4@cluster0.pmbm4ny.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_connect, tlsCAFile=certifi.where())
db = client.temp

phone = '01000000001'
pw = 'test1234'
try:
    db_data = list(db.account.find({'phone':{'$regex': phone}}))
    user_data = dict(db_data[0])
    password_db = user_data['pw']

    if(pw == password_db):
        response = {"message":"login success"} #,"status": HTTPStatus.OK
        print (response)
    else:
        response = {"message":"login failed: passwrod wrong"} #,"status": HTTPStatus.OK
        print (response)

except:
    response = {"message":"login failed: none phone number"}#,"status": HTTPStatus.OK
    print( response )