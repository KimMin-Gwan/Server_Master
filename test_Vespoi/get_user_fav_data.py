import requests
from urllib.parse import urlparse
import json
import back_end
from pymongo import MongoClient
import certifi

class GetFav():
    def __init__(self,phone):
        self.phone = phone
    
    def get_fav(self):
        mongo_connect = "mongodb+srv://admin:r3tgCfkESORu8iO4@cluster0.pmbm4ny.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(mongo_connect, tlsCAFile=certifi.where())
        db = client.temp
        try:
            db_data = list(db.user_data.find({'phone':{'$regex': self.phone}}))
            user_data = dict(db_data[0])
            fav_data = user_data['fav']

            response = {"message":fav_data} 
            return response

        except:
            response = {"message":"unknown error"}
            return response