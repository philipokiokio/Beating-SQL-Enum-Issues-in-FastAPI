from fastapi import FastAPI, status, HTTPException,Depends
from app.database import get_db,engine
from app import models, schemas
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)



app = FastAPI()



@app.post('/survey/create', status_code= status.HTTP_201_CREATED, response_model=schemas.SurveyResponse)
def create_survey(survey_data:schemas.SurveyCreate, db:Session= Depends(get_db)):
    
    email_check = db.query(models.Survey).filter(models.Survey.email == survey_data.email).first()
    
    if email_check:
        raise HTTPException(
            status_code= status.HTTP_409_CONFLICT,
            detail='This Email is already attached to a survey, click edit to update your answers'
        )

    new_survey= models.Survey(**survey_data.dict())
    db.add(new_survey)
    db.commit()
    db.refresh(new_survey)
    return {
        'message': "Survey Information saved in our DB",
        'data': new_survey,
        'status':status.HTTP_201_CREATED
    }
    










@app.get('/')
def root():
    return {
        "msg": "This Groot, the server."
    }