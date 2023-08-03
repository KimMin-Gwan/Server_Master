from pydantic import BaseModel

# GPS 데이터 형식
class GPS(BaseModel):
    x:float
    y:float



