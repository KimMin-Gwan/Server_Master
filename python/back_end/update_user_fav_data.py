import requests
from urllib.parse import urlparse
import json
import back_end
from pymongo import MongoClient
import certifi

class UpdateFav():
    def __init__(self, phone, fave_data): #fav_data는 list
        self.phone = phone
        self.fav_data = fave_data
    
    def update_fav(self):
        mongo_connect = "mongodb+srv://admin:r3tgCfkESORu8iO4@cluster0.pmbm4ny.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(mongo_connect, tlsCAFile=certifi.where())
        db = client.temp

        try:
            db.user_data.update_one({"phone" :self.phone},{'$set' : {"fav":self.fav_data}})

            response = {"message":"saved"} 
            return response

        except:
            response = {"message":"unknown error"}
            return response
    