import requests
from urllib.parse import urlparse
import json
from pymongo import MongoClient
import certifi

mongo_connect = "mongodb+srv://admin:r3tgCfkESORu8iO4@cluster0.pmbm4ny.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_connect, tlsCAFile=certifi.where())
db = client.temp
data={
    'name': 'mtest',
    'phone': '01000000001',
    'pw': 'test1234'
}

try:
    db.account.insert_one(data)

except:
    response = {"message":"register failed"}
    print( response)
        
response = {"message":"register success"}
print( response)