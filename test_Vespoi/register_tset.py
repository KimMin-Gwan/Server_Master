import requests
from urllib.parse import urlparse
import json
from pymongo import MongoClient
import certifi

phone = '01010012002'
def check_dupe():
    mongo_connect = "mongodb+srv://admin:r3tgCfkESORu8iO4@cluster0.pmbm4ny.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(mongo_connect, tlsCAFile=certifi.where())
    db = client.temp

    try: 
        db_data = list(db.account.find({'phone':{'$regex': phone}}))
        if(len(phone)!=11):
            print(db_data, 'invalid')
            return True

        elif not db_data:
            print(db_data, 'empty')
            return False
        else:
            print(db_data, 'not empty')
            return True
    except:
        print("none")
        return False

mongo_connect = "mongodb+srv://admin:r3tgCfkESORu8iO4@cluster0.pmbm4ny.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_connect, tlsCAFile=certifi.where())
db = client.temp
data={
    'name': 'localdutetest',
    'phone': phone,
    'pw': 'test1234'
}

check_reg = check_dupe()
if(check_reg==True):
    response = {"message":"register failed phone already exists or invalid number"}
    print(len(data['phone']))
    print( response)

else:
    try:
        db.account.insert_one(data)
        response = {"message":"register success"}
        print( response)

    except:
        response = {"message":"register failed"}
        print( response)


        
