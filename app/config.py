from pydantic import BaseSettings


class Settings(BaseSettings):
    database_name :str
    database_username:str
    database_password:str
    database_hostname:str
    
    class Config:
        env_file= '.env'
    
settings = Settings()