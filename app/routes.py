from fastapi import APIRouter
from app.schemas import HouseInput
from app.model import model
import numpy as np 
import pandas as pd

router = APIRouter()

@router.post("/predict")

def house_price(data : HouseInput) :
    
    # x = pd.DataFrame([data.dict()])
    x = pd.DataFrame([data.features])

    



    prediction=model.predict(x)
    return{f'prediction':int(prediction[0])}
    