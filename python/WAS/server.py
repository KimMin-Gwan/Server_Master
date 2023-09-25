from fastapi import FastAPI
#from fastapi.responses import FileResponse
from fastapi import UploadFile, File
import WAS
import uvicorn
#from constant import WAV_SAVE_PATH

class AppServer():
    def __init__(self, mainfunction):
        self.app = FastAPI()
        self.mainfunction = mainfunction
        self.register_routes()

    def register_routes(self):
        #wav 데이터 받기
        @self.app.post('/get_string')
        async def recog_voice(data : dict):
            if data is None:
                print('data did not uploaded')
                return {"key": "ERROR"} 
            else:
                print('json loaded')
            try:
                print("incomming data : ",data)
                result = self.mainfunction.recog_wav(data['key'])
            except Exception as e:
                print("Error : ", str(e))

            if result['key'] == 'ERROR':
                return {"error" : "Recognize Fail"}

            return result # {'key' : data}


        #GPS 데이터 보내기
        @self.app.post('/get_gps')
        async def recog_GPS(data : dict):
            if data is None:
                print('gps not uploaded')
                return {"error": "data did not usable"}

            x = float(data['x'])
            y = float(data['y'])

            try:
                result = self.mainfunction.recog_gps(x, y)
            except Exception as e:
                print("Erro : ", str(e))

            return result

        @self.app.post('/login')
        async def login(data : dict):
            if data is None:
                print('login data none')
                return {"message":"login failed"} #,"status": HTTPStatus.OK
            
            phone = data['phone']
            pw = data['password']
            
            try:
                result = self.mainfunction.login_req(phone, pw)
            except Exception as e:
                print("Error : ", str(e))

            return result

        @self.app.post('/register')
        async def register(data : dict):
            if data is None:
                print('register data none')
                return {"message":"register failed"} #,"status": HTTPStatus.OK

            name = data['name']
            phone = data['phone']
            pw = data['password']
            
            try:
                result = self.mainfunction.register_req(name, phone, pw)
            except Exception as e:
                print("Error : ", str(e))

            return result

        @self.app.post('/update_fav')
        async def register(data : dict):
            if data is None:
                print('fav data none')
                return {"message":"update data failed"} 

            phone = data['phone']
            fav_data = data['fav']
            
            try:
                result = self.mainfunction.update_user_fav_data(phone, fav_data)
            except Exception as e:
                print("Error : ", str(e))

            return result

        @self.app.post('/get_fav')
        async def register(data : dict):
            if data is None:
                print('fav data none')
                return {"message":"load data failed"} #,"status": HTTPStatus.OK

            phone = data['phone']
            
            try:
                result = self.mainfunction.get_user_fav_data(phone)
            except Exception as e:
                print("Error : ", str(e))

            return result

        
    def run_server(self, HOST, PORT):
        uvicorn.run(self.app, host=HOST, port= PORT)



        
    
