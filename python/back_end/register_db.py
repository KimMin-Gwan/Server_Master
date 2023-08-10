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

    def __check_dupe(self):
        mongo_connect = back_end.constant.mongo_key
        client = MongoClient(mongo_connect, tlsCAFile=certifi.where())
        db = client.temp

        try: 
            db_data = list(db.account.find({'phone':{'$regex': self.phone}}))
            if not db_data:
                return False #리스트가 비어있음 ( 데이터 없음 )
            else:
                return True #리스트에 정보가 있음
        except: 
            return False # 못찾음

    def register(self):
        #db 연결
        mongo_connect = back_end.constant.mongo_key
        client = MongoClient(mongo_connect, tlsCAFile=certifi.where())
        db = client.temp

        #db에 넘길 데이터
        data={
            'name': self.name,
            'phone': self.phone,
            'pw': self.pw
            }
        
        #중복확인
        check_reg = self.__check_dupe()

        if(check_reg==True): #이미 있으면 실패
            response = {"message":"register failed phone already exists"}
            return response
        
        else:
            try: #없으면 추가
                db.account.insert_one(data)
                response = {"message":"register success"} #,"status": HTTPStatus.OK
                return response

            except: #없지만 뭔가 문제가 생김 (잘못된? 데이터)
                response = {"message":"register failed"} #,"status": HTTPStatus.OK
                return response
        #몰?루
        response = {"message":"unknown error"}
        return response
        
        
