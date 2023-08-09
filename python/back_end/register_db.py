import requests
from urllib.parse import urlparse
import json
import back_end
from pymongo import MongoClient
import certifi

class Register():
    def __init__(self, name, phone, pw):
        self.name = name
        self.phone = phone
        self.pw = pw

    def register(self):
        mongo_connect = back_end.constant.mongo_key
        client = MongoClient(mongo_connect, tlsCAFile=certifi.where())
        db = client.temp

        data={
            'name': self.name,
            'phone': self.phone,
            'pw': self.pw
            }

        try:
            db.account.insert_one(data)

        except:
            response = {"message":"register failed"} #,"status": HTTPStatus.OK
            return response
        
        response = {"message":"register success"} #,"status": HTTPStatus.OK
        return response
