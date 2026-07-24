from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class InsuranceApplication(BaseModel):
    name:str
    age:int
    height:float
    weight:float
    smoker:bool
    diabetic:bool
    excercise:bool
    annual_income:float

@app.post("/health-insurance")
def calculate_premium(application:InsuranceApplication):
    height_meter=application.height/100
    bmi=application.weight/(height_meter**2)
    risk_score=0
    if application.smoker:
        risk_score+=3
    if application.diabetic:
        risk_score+=2
    if bmi>30:
        risk_score+=2
    if application.age>50:
        risk_score+=2
    if not application.excercise:
        risk_score+=1

    if risk_score <= 2:
        risk = "Low"
        premium = 5000

    elif risk_score <= 5:
        risk = "Medium"
        premium = 8000

    else:
        risk = "High"
        premium = 12000

    eligible=application.age<=65

    return {
        "name": application.name,
        "age": application.age,
        "BMI": round(bmi, 2),
        "risk_score": risk_score,
        "risk": risk,
        "premium": premium,
        "eligible": eligible
    }
