from pydantic import BaseModel,EmailStr
from enum import Enum
from datetime import datetime


class SocialEnum(str,Enum):
    twitter= 'Twitter'
    facebook = 'Facebook'
    tik_tok= 'Tik Tok'
    instagram='Instagram'

class ContinentEnum(str,Enum):
    africa = 'Africa'
    europe= 'Europe'
    others = 'Others'

class MoneyEnum(str, Enum):
    usd= 'USD'
    usdc = 'USDC'
    others ='Others'
    
    


class Survey(BaseModel):
    email: EmailStr
    social: SocialEnum= SocialEnum.twitter
    continent: ContinentEnum = ContinentEnum.africa
    money:MoneyEnum= MoneyEnum.usd
    
    
class SurveyCreate(Survey):
    pass 


class SurveyDB_Data(Survey):
    id:int
    created_at: datetime
    
    class Config:
        orm_mode= True        

class SurveyResponse(BaseModel):
    message:str
    data: SurveyDB_Data
    status:int
    
    

        


