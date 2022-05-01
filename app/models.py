from enum import unique
from sqlalchemy import Column,Integer, String,TIMESTAMP
from sqlalchemy.sql.expression import text
from app.database import Base
# from enum import Enum
# This is a special import for ENUM strictly because I am using postgres DB
# from sqlalchemy.dialects.postgresql import ENUM




# class SocialEnum(Enum):
#     twitter= 'Twitter'
#     facebook = 'Facebook'
#     instagram='Instagram'

# class ContinentEnum(Enum):
#     africa = 'Africa'
#     others = 'Others'

# class MoneyEnum(Enum):
#     usd= 'USD'
#     others ='Others'

# Commented out so you can see it was once used as mentioned on the post.


class Survey(Base):
    __tablename__ ='fast_survey'
    id = Column(Integer, primary_key= True, index=True)
    email = Column(String, unique=True, nullable=False)
    social= Column(String,nullable= False)
    continent= Column(String, nullable= False)
    money= Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))